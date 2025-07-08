"""Basic logging utilities."""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:
    """Simple logger wrapper used throughout the application."""

    def __init__(self, name: str = __name__, log_file: str = "data/logs/scraper.log") -> None:
        """Create a new ``Logger`` instance.

        Args:
            name: Logger name used when emitting log entries.
            log_file: Path to the log file.
        """
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        self._logger = logging.getLogger(name)
        self._logger.setLevel(logging.INFO)
        if not self._logger.handlers:
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)
            self._logger.addHandler(stream_handler)

    def log(self, message: str, level: int = logging.INFO) -> None:
        """Log a message at the specified level.

        Args:
            message: Text message to log.
            level: Logging level from the :mod:`logging` module.
        """
        self._logger.log(level, message)
