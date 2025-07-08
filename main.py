import time

from src.scheduling.schedule_manager import ScheduleManager


def dummy_job() -> None:
    """Example job that prints a message."""

    print("Dummy job executed")


def main() -> None:
    """Run the simple command-line scheduler demo."""

    manager = ScheduleManager()
    manager.add_task("dummy", dummy_job, 5)

    print("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            manager.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nScheduler stopped.")


if __name__ == "__main__":
    main()

