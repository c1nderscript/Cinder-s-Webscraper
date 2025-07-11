
"""High-level interface for managing recurring tasks with SQLite persistence."""


from __future__ import annotations

import importlib
import os
import sqlite3
from typing import Callable, Dict, List, Optional

import schedule

from cinder_web_scraper.utils.logger import default_logger as logger


class ScheduleManager:

    """Manage scheduled jobs using the :mod:`schedule` package with SQLite persistence.

    The manager can be used as a context manager to ensure the underlying
    SQLite connection is closed automatically::

        with ScheduleManager() as manager:
            manager.add_task("dummy", dummy_job, 5)
            manager.run_pending()

    When the ``with`` block exits, :pymeth:`close` is called automatically.
    """

    def __init__(self, db_path: str = "data/schedules.db") -> None:
        """Initialize the manager and load any stored tasks.

        Args:
            db_path: Location of the SQLite database file.
        """


        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path) or ".", exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()

        self.jobs: Dict[str, schedule.Job] = {}
        self._load_tasks()
        logger.log("ScheduleManager initialized")

    # ------------------------------------------------------------------
    # SQLite helpers
    # ------------------------------------------------------------------
    def _init_db(self) -> None:
        """Create required tables if they don't exist."""
        with self.conn:
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS schedules (
                    name TEXT PRIMARY KEY,
                    interval INTEGER NOT NULL
                )
                """
            )
            self.conn.execute(
                """
                CREATE TABLE IF NOT EXISTS tasks (
                    name TEXT PRIMARY KEY,
                    module TEXT NOT NULL,
                    func_name TEXT NOT NULL,
                    interval INTEGER NOT NULL
                )
                """
            )

    def _load_tasks(self) -> None:
        """Load persisted tasks from the database."""
        cursor = self.conn.execute(
            "SELECT name, module, func_name, interval FROM tasks"
        )
        for name, module, func_name, interval in cursor.fetchall():
            try:
                mod = importlib.import_module(module)
                func = getattr(mod, func_name)
            except Exception as exc:  # pragma: no cover - invalid modules ignored
                logger.error(
                    f"Failed to import task '{name}' from {module}:{func_name}: {exc}"
                )
                continue

            job = schedule.every(interval).seconds.do(func)
            self.jobs[name] = job

    def _persist_task(
        self, name: str, func: Callable[..., object], interval: int
    ) -> None:
        """Persist a task definition to the database."""
        with self.conn:
            self.conn.execute(
                """
                INSERT OR REPLACE INTO tasks (name, module, func_name, interval)
                VALUES (?, ?, ?, ?)
                """,
                (name, func.__module__, func.__name__, interval),
            )
            self.conn.execute(
                "INSERT OR REPLACE INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )

    def _delete_task(self, name: str) -> None:
        """Remove a task from the database."""
        with self.conn:
            self.conn.execute("DELETE FROM tasks WHERE name = ?", (name,))
            self.conn.execute("DELETE FROM schedules WHERE name = ?", (name,))

    # ------------------------------------------------------------------
    # Public CRUD API
    # ------------------------------------------------------------------
    def create_schedule(self, name: str, interval: int) -> None:
        """Insert a schedule record."""
        with self.conn:
            self.conn.execute(
                "INSERT INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )

    def get_schedule(self, name: str) -> Optional[Dict[str, int]]:
        """Retrieve a schedule record by ``name``."""
        cur = self.conn.execute(
            "SELECT name, interval FROM schedules WHERE name = ?",
            (name,),
        )
        row = cur.fetchone()
        if row:
            return {"name": row["name"], "interval": row["interval"]}
        return None

    def update_schedule(self, name: str, interval: int) -> bool:
        """Update the ``interval`` for a schedule."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE schedules SET interval = ? WHERE name = ?",
                (interval, name),
            )
            updated = cur.rowcount > 0
        if updated and name in self.jobs:
            func = self.jobs[name].job_func
            if hasattr(func, "func"):
                func = func.func
            schedule.cancel_job(self.jobs[name])
            self.jobs[name] = schedule.every(interval).seconds.do(func)
        return updated

    def delete_schedule(self, name: str) -> bool:
        """Delete a schedule record."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM schedules WHERE name = ?",
                (name,),
            )
            return cur.rowcount > 0

    def list_schedules(self) -> List[Dict[str, int]]:
        """Return all schedules stored in the database."""
        cur = self.conn.execute("SELECT name, interval FROM schedules")
        return [
            {"name": row["name"], "interval": row["interval"]}
            for row in cur.fetchall()
        ]

    # ------------------------------------------------------------------
    # Task scheduling API
    # ------------------------------------------------------------------
    def add_task(
        self, name: str, func: Callable[..., object], interval: int
    ) -> schedule.Job:
        """Add a job that runs every ``interval`` seconds and persist it."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        logger.log(f"Added task '{name}' to run every {interval} seconds")

        self._persist_task(name, func, interval)
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled job by ``name`` and delete its record."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            self._delete_task(name)
            logger.log(f"Removed task '{name}'")
            return True
        logger.log(f"Attempted to remove unknown task '{name}'")
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        """Return a mapping of task names to jobs."""
        logger.log("Listing scheduled tasks")
        return dict(self.jobs)

    def run_pending(self) -> None:
        """Execute any tasks that are due to run."""
        logger.log("Running pending scheduled tasks")
        schedule.run_pending()

    def close(self) -> None:
        """Close the underlying SQLite connection."""
        self.conn.close()

    def __enter__(self) -> "ScheduleManager":
        """Return the manager instance for context manager support."""
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        """Close the SQLite connection when exiting a ``with`` block."""
        self.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass
