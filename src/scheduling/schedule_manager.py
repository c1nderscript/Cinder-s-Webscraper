"""High-level interface for managing recurring tasks."""

import schedule
from typing import Callable, Dict

from src.utils.logger import default_logger as logger


class ScheduleManager:
    """Manage scheduled jobs using the schedule package."""

    def __init__(self) -> None:
        self.jobs: Dict[str, schedule.Job] = {}

    def add_task(self, name: str, func: Callable, interval: int) -> schedule.Job:
        """Add a job that runs every ``interval`` seconds."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        logger.log(f"Added task '{name}' to run every {interval} seconds")
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled job by name."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            logger.log(f"Removed task '{name}'")
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

