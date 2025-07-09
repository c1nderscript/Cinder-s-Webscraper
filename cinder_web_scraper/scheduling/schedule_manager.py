"""SQLite-backed scheduler integration using the :mod:`schedule` library."""

from __future__ import annotations

import importlib
import os
import sqlite3
from typing import Callable, Dict, List, Optional

import schedule

from src.utils.logger import default_logger as logger


class ScheduleManager:
    """Manage scheduled tasks with persistent storage."""

    def __init__(self, db_path: str = "data/schedules.db") -> None:
        """Initialize the manager and load any persisted tasks.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path) or ".", exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self._init_db()
        self.jobs: Dict[str, schedule.Job] = {}
        self._load_tasks()

    # ------------------------------------------------------------------
    # Database setup and loading
    # ------------------------------------------------------------------
    def _init_db(self) -> None:
        """Create required tables if they do not exist."""
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
        """Load tasks from the database and schedule them."""
        cursor = self.conn.execute(
            "SELECT name, module, func_name, interval FROM tasks"
        )
        for row in cursor.fetchall():
            try:
                module = importlib.import_module(row["module"])
                func = getattr(module, row["func_name"])
            except Exception as exc:  # pragma: no cover - invalid entries
                logger.error(f"Failed loading task {row['name']}: {exc}")
                continue
            job = schedule.every(row["interval"]).seconds.do(func)
            self.jobs[row["name"]] = job

    # ------------------------------------------------------------------
    # Schedule CRUD operations
    # ------------------------------------------------------------------
    def create_schedule(self, name: str, interval: int) -> None:
        """Create a new schedule entry."""
        with self.conn:
            self.conn.execute(
                "INSERT INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )

    def get_schedule(self, name: str) -> Optional[Dict[str, int]]:
        """Return a schedule entry if it exists."""
        cur = self.conn.execute(
            "SELECT name, interval FROM schedules WHERE name = ?",
            (name,),
        )
        row = cur.fetchone()
        if row:
            return {"name": row["name"], "interval": row["interval"]}
        return None

    def update_schedule(self, name: str, interval: int) -> bool:
        """Update an existing schedule's interval."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE schedules SET interval = ? WHERE name = ?",
                (interval, name),
            )
            return cur.rowcount > 0

    def delete_schedule(self, name: str) -> bool:
        """Remove a schedule entry."""
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM schedules WHERE name = ?",
                (name,),
            )
            return cur.rowcount > 0

    def list_schedules(self) -> List[Dict[str, int]]:
        """Return all saved schedules."""
        cur = self.conn.execute("SELECT name, interval FROM schedules")
        return [
            {"name": row["name"], "interval": row["interval"]}
            for row in cur.fetchall()
        ]

    # ------------------------------------------------------------------
    # Task management
    # ------------------------------------------------------------------
    def _persist_task(
        self, name: str, func: Callable[..., None], interval: int
    ) -> None:
        """Persist task details to the database."""
        with self.conn:
            self.conn.execute(
                """
                INSERT OR REPLACE INTO tasks (name, module, func_name, interval)
                VALUES (?, ?, ?, ?)
                """,
                (name, func.__module__, func.__name__, interval),
            )

    def _delete_task(self, name: str) -> None:
        """Delete a task record from the database."""
        with self.conn:
            self.conn.execute("DELETE FROM tasks WHERE name = ?", (name,))

    def add_task(
        self, name: str, func: Callable[..., None], interval: int
    ) -> schedule.Job:
        """Schedule ``func`` to run every ``interval`` seconds."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        self._persist_task(name, func, interval)
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )
        logger.info(f"Added task '{name}' to run every {interval} seconds")
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled task."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            self._delete_task(name)
            self.delete_schedule(name)
            logger.info(f"Removed task '{name}'")
            return True
        logger.warning(f"Attempted to remove unknown task '{name}'")
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        """Return a mapping of task names to scheduled jobs."""
        return dict(self.jobs)

    def run_pending(self) -> None:
        """Run all pending scheduled jobs."""
        schedule.run_pending()

    def close(self) -> None:
        """Close the underlying database connection."""
        self.conn.close()

    def __del__(self) -> None:  # pragma: no cover - cleanup
        try:
            self.close()
        except Exception:
            pass
