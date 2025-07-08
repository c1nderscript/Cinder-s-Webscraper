"""High-level interface for managing recurring tasks with persistence."""

import importlib
import os
import sqlite3
from typing import Callable, Dict

import schedule


class ScheduleManager:
    """Manage scheduled jobs using the schedule package with SQLite persistence."""

    def __init__(self, db_path: str = "data/schedules.db") -> None:
        self.db_path = db_path
        self.jobs: Dict[str, schedule.Job] = {}
        self._init_db()
        self._load_tasks()

    def add_task(
        self, name: str, func: Callable, interval: int
    ) -> schedule.Job:
        """Add a job that runs every ``interval`` seconds and persist it."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        self._save_task(name, func, interval)
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled job by name."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            self._delete_task(name)
            return True
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        """Return a mapping of task names to jobs."""
        return dict(self.jobs)

    def run_pending(self) -> None:
        """Run all jobs that are scheduled to run."""
        schedule.run_pending()

    # ------------------------------------------------------------------
    # Persistence helpers
    # ------------------------------------------------------------------

    def _init_db(self) -> None:
        """Initialize the schedules database."""
        os.makedirs(os.path.dirname(self.db_path) or ".", exist_ok=True)
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS tasks ("
                "name TEXT PRIMARY KEY,"
                "module TEXT NOT NULL,"
                "function TEXT NOT NULL,"
                "interval INTEGER NOT NULL"
                ")"
            )

    def _save_task(self, name: str, func: Callable, interval: int) -> None:
        """Persist a task definition to the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "REPLACE INTO tasks (name, module, function, interval) VALUES (?, ?, ?, ?)",
                (name, func.__module__, func.__name__, interval),
            )

    def _delete_task(self, name: str) -> None:
        """Remove a task from the database."""
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("DELETE FROM tasks WHERE name = ?", (name,))

    def _load_tasks(self) -> None:
        """Load tasks from the database and schedule them."""
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT name, module, function, interval FROM tasks"
            ).fetchall()

        for name, module_name, func_name, interval in rows:
            try:
                module = importlib.import_module(module_name)
                func = getattr(module, func_name)
            except Exception:
                # Skip invalid task definitions
                continue
            job = schedule.every(interval).seconds.do(func)
            self.jobs[name] = job
