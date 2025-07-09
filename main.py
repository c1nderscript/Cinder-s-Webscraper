"""Command-line entry point for running scheduled jobs."""

from __future__ import annotations

import time
import traceback

from cinder_web_scraper.scheduling.schedule_manager import ScheduleManager
from cinder_web_scraper.utils.logger import default_logger as logger


def dummy_job() -> None:
    """Example job that prints a message."""
    logger.log("Dummy job executed")


def main() -> None:
    """Run the simple command-line scheduler demo with persistence and error handling."""
    manager = ScheduleManager()

    if not manager.list_tasks():
        manager.add_task("dummy", dummy_job, 5)

    logger.log("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            manager.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.log("Scheduler stopped.")
        print("\nScheduler stopped.")
    except Exception as exc:  # pragma: no cover - runtime errors
        print("An unexpected error occurred. See log for details.")
        logger.error("Unhandled exception in CLI")
        logger.error(traceback.format_exc())
    finally:
        manager.close()


if __name__ == "__main__":
    main()
