"""Simple wrapper around the ``schedule`` package with SQLite persistence."""

from __future__ import annotations

import importlib
import os
import sqlite3
from typing import Callable, Dict, List, Optional

import schedule

from src.utils.logger import default_logger as logger


class ScheduleManager:
    """Manage scheduled tasks and persist them to SQLite."""

    def __init__(self, db_path: str = "data/schedules.db") -> None:
        self.db_path = db_path
        os.makedirs(os.path.dirname(self.db_path) or ".", exist_ok=True)
        self.conn = sqlite3.connect(self.db_path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute(
            """
            CREATE TABLE IF NOT EXISTS schedules (
                name TEXT PRIMARY KEY,
                module TEXT NOT NULL,
                func_name TEXT NOT NULL,
                interval INTEGER NOT NULL
            )
            """
        )
        self.conn.commit()
        self.jobs: Dict[str, schedule.Job] = {}
        self._load_tasks()

    # ------------------------------------------------------------------
    # database helpers
    # ------------------------------------------------------------------

    def _load_tasks(self) -> None:
        """Load persisted tasks from the database."""
        cursor = self.conn.execute(
            "SELECT name, module, func_name, interval FROM schedules"
        )
        for name, module, func_name, interval in cursor.fetchall():
            try:
                mod = importlib.import_module(module)
                func = getattr(mod, func_name)
            except Exception:
                # Skip tasks that cannot be imported
                continue
            job = schedule.every(interval).seconds.do(func)
            self.jobs[name] = job

    # ------------------------------------------------------------------
    # CRUD operations
    # ------------------------------------------------------------------

    def create_schedule(self, name: str, interval: int) -> None:
        with self.conn:
            self.conn.execute(
                "INSERT INTO schedules (name, module, func_name, interval) VALUES (?, ?, ?, ?)",
                (name, "", "", interval),
            )

    def get_schedule(self, name: str) -> Optional[Dict[str, int]]:
        cur = self.conn.execute(
            "SELECT name, interval FROM schedules WHERE name = ?",
            (name,),
        )
        row = cur.fetchone()
        if row:
            return {"name": row["name"], "interval": row["interval"]}
        return None

    def update_schedule(self, name: str, interval: int) -> bool:
        with self.conn:
            cur = self.conn.execute(
                "UPDATE schedules SET interval = ? WHERE name = ?",
                (interval, name),
            )
            return cur.rowcount > 0

    def delete_schedule(self, name: str) -> bool:
        with self.conn:
            cur = self.conn.execute(
                "DELETE FROM schedules WHERE name = ?",
                (name,),
            )
            return cur.rowcount > 0

    def list_schedules(self) -> List[Dict[str, int]]:
        cur = self.conn.execute("SELECT name, interval FROM schedules")
        return [
            {"name": row["name"], "interval": row["interval"]}
            for row in cur.fetchall()
        ]

    # ------------------------------------------------------------------
    # scheduling operations
    # ------------------------------------------------------------------

    def add_task(self, name: str, func: Callable, interval: int) -> schedule.Job:
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO schedules (name, module, func_name, interval) VALUES (?, ?, ?, ?)",
                (name, func.__module__, func.__name__, interval),
            )
        logger.log(f"Added task '{name}' to run every {interval} seconds")
        return job

    def remove_task(self, name: str) -> bool:
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            self.delete_schedule(name)
            logger.log(f"Removed task '{name}'")
            return True
        logger.log(f"Attempted to remove unknown task '{name}'")
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        logger.log("Listing scheduled tasks")
        return dict(self.jobs)

    def run_pending(self) -> None:
        logger.log("Running pending scheduled tasks")
        schedule.run_pending()

    def close(self) -> None:
        self.conn.close()

    def __del__(self) -> None:  # pragma: no cover - cleanup
        try:
            self.conn.close()
        except Exception:
            pass
