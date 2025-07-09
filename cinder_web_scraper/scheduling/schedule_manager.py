"""High-level interface for managing recurring tasks with persistence."""

from __future__ import annotations

import importlib
import os
import sqlite3
from typing import Callable, Dict, List, Optional

import schedule

from cinder_web_scraper.utils.logger import default_logger as logger


class ScheduleManager:
    """Manage scheduled jobs using the schedule package and SQLite."""

    def __init__(self, db_path: str = "data/schedules.db") -> None:
        """Initialize the manager, create tables and load persisted tasks."""
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path) or ".", exist_ok=True)

        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row

        self._init_db()
        self.jobs: Dict[str, schedule.Job] = {}
        self._load_tasks()

    # ------------------------------------------------------------------
    # database handling
    # ------------------------------------------------------------------
    def _init_db(self) -> None:
        """Create required tables if they don't exist."""
        with self.conn:
            self.conn.execute(
                "CREATE TABLE IF NOT EXISTS schedules (name TEXT PRIMARY KEY, interval INTEGER)"
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
        """Load all persisted tasks from the database."""
        cursor = self.conn.execute(
            "SELECT name, module, func_name, interval FROM tasks"
        )
        for name, module, func_name, interval in cursor.fetchall():
            try:
                mod = importlib.import_module(module)
                func = getattr(mod, func_name)
            except Exception:
                # Skip tasks that can't be imported
                continue
            job = schedule.every(interval).seconds.do(func)
            self.jobs[name] = job

    def _persist_task(self, name: str, func: Callable, interval: int) -> None:
        """Persist a task definition to the database."""
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO tasks (name, module, func_name, interval)"
                " VALUES (?, ?, ?, ?)",
                (name, func.__module__, func.__name__, interval),
            )

    def _delete_task(self, name: str) -> None:
        """Remove a task from the database."""
        with self.conn:
            self.conn.execute("DELETE FROM tasks WHERE name = ?", (name,))

    # ------------------------------------------------------------------
    # schedules table CRUD
    # ------------------------------------------------------------------
    def create_schedule(self, name: str, interval: int) -> None:
        """Insert a schedule record."""
        with self.conn:
            self.conn.execute(
                "INSERT INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )

    def get_schedule(self, name: str) -> Optional[Dict[str, int]]:
        """Retrieve a schedule record by name."""
        cur = self.conn.execute(
            "SELECT name, interval FROM schedules WHERE name = ?",
            (name,),
        )
        row = cur.fetchone()
        if row:
            return {"name": row["name"], "interval": row["interval"]}
        return None

    def update_schedule(self, name: str, interval: int) -> bool:
        """Update the interval for a schedule."""
        with self.conn:
            cur = self.conn.execute(
                "UPDATE schedules SET interval = ? WHERE name = ?",
                (interval, name),
            )
            return cur.rowcount > 0

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
    # task scheduling operations
    # ------------------------------------------------------------------
    def add_task(self, name: str, func: Callable, interval: int) -> schedule.Job:
        """Add a job that runs every ``interval`` seconds and persist it."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        logger.log(f"Added task '{name}' to run every {interval} seconds")

        self._persist_task(name, func, interval)
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO schedules (name, interval) VALUES (?, ?)",
                (name, interval),
            )
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled job by name."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            logger.log(f"Removed task '{name}'")
            self._delete_task(name)
            self.delete_schedule(name)
            return True
        logger.log(f"Attempted to remove unknown task '{name}'")
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        """Return a mapping of task names to jobs."""
        logger.log("Listing scheduled tasks")
        return dict(self.jobs)

    def run_pending(self) -> None:
        """Run all jobs that are scheduled to run."""
        logger.log("Running pending scheduled tasks")
        schedule.run_pending()

    def close(self) -> None:
        """Close the underlying SQLite connection."""
        self.conn.close()

    def __del__(self) -> None:
        try:
            self.close()
        except Exception:
            pass
