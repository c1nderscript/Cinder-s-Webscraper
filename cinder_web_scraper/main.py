from __future__ import annotations

import argparse
import logging
import time
import traceback

from cinder_web_scraper.gui.main_window import MainWindow
from cinder_web_scraper.scheduling.schedule_manager import ScheduleManager
from cinder_web_scraper.utils.logger import default_logger as logger


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed options.
    """
    parser = argparse.ArgumentParser(description="Cinder's Web Scraper")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--gui", action="store_true", help="Launch in GUI mode")
    group.add_argument("--cli", action="store_true", help="Launch in CLI mode")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")
    return parser.parse_args()


def run_cli() -> None:
    """Execute the command-line scheduler loop."""
    manager = ScheduleManager()
    if not manager.list_tasks():
        manager.add_task("dummy", lambda: logger.log("Dummy job executed"), 5)

    logger.log("Scheduler started. Press Ctrl+C to exit.")
    try:
        while True:
            manager.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        logger.log("Scheduler stopped.")
        print("\nScheduler stopped.")
    except Exception as exc:  # pragma: no cover
        print("An unexpected error occurred. See log for details.")
        logger.error("Unhandled exception in CLI")
        logger.error(traceback.format_exc())
    finally:
        manager.close()


def run_gui() -> None:
    """Launch the GUI application."""
    window = MainWindow()
    window.show()


def main() -> None:
    """Application entry point.

    Parses command-line options and launches either the CLI or GUI.
    """
    args = parse_arguments()
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    if args.cli:
        run_cli()
    else:
        run_gui()


if __name__ == "__main__":
    main()

