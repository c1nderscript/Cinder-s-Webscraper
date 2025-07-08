"""Command-line entry point for running scheduled jobs."""

from __future__ import annotations

import time
import traceback

from src.scheduling.schedule_manager import ScheduleManager
from src.utils.logger import get_logger


def dummy_job() -> None:
    """Example job that prints a message."""

    print("Dummy job executed")


logger = get_logger(__name__)


def main() -> None:
    """Run the simple command-line scheduler demo with persistence and error handling."""

    manager = ScheduleManager()

    if not manager.list_tasks():
        manager.add_task("dummy", dummy_job, 5)

    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            manager.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")
    except Exception as exc:  # pragma: no cover - runtime errors
        print("An unexpected error occurred. See log for details.")
        logger.error("Unhandled exception in CLI")
        logger.error(traceback.format_exc())
    finally:
        manager.close()


if __name__ == "__main__":
    main()

