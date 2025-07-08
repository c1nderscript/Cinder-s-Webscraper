"""Application logging utilities."""

from __future__ import annotations

import logging
from pathlib import Path


class Logger:
    """Wrapper around :mod:`logging` with predefined configuration."""

    def __init__(
        self, name: str = __name__, log_file: str = "data/logs/scraper.log"
    ) -> None:
        """Configure a logger instance.

        Args:
            name: Name of the logger to create.
            log_file: Path to the log file.
        """
        path = Path(log_file)
        path.parent.mkdir(parents=True, exist_ok=True)

        self._logger = logging.getLogger(name)
        if not self._logger.handlers:
            self._logger.setLevel(logging.INFO)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            file_handler = logging.FileHandler(path)
            stream_handler = logging.StreamHandler()
            file_handler.setFormatter(formatter)
            stream_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)
            self._logger.addHandler(stream_handler)

    def info(self, message: str) -> None:
        """Log an informational ``message``."""

        self._logger.info(message)

    def warning(self, message: str) -> None:
        """Log a warning ``message``."""

        self._logger.warning(message)

    def error(self, message: str) -> None:
        """Log an error ``message``."""

        self._logger.error(message)
