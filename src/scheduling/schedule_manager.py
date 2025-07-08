import schedule
from typing import Callable, Dict


class ScheduleManager:
    """Manage scheduled jobs using the schedule package."""

    def __init__(self) -> None:
        self.jobs: Dict[str, schedule.Job] = {}

    def add_task(self, name: str, func: Callable, interval: int) -> schedule.Job:
        """Add a job that runs every ``interval`` seconds."""
        job = schedule.every(interval).seconds.do(func)
        self.jobs[name] = job
        return job

    def remove_task(self, name: str) -> bool:
        """Remove a scheduled job by name."""
        job = self.jobs.pop(name, None)
        if job:
            schedule.cancel_job(job)
            return True
        return False

    def list_tasks(self) -> Dict[str, schedule.Job]:
        """Return a mapping of task names to jobs."""
        return dict(self.jobs)

    def run_pending(self) -> None:
        """Run all jobs that are scheduled to run."""
        schedule.run_pending()

