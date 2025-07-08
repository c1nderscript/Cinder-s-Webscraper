"""Logging utilities used across the application."""

from __future__ import annotations

import logging
from pathlib import Path

# Ensure the log directory exists
LOG_FILE = Path("data/logs/scraper.log")
LOG_FILE.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(),
    ],
)


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

    def log(self, message: str, level: str = "info") -> None:
        """Log a message at the specified level.

        Args:
            message: The message to log.
            level: The logging level (debug, info, warning, error, critical).
        """
        level_map = {
            "debug": self._logger.debug,
            "info": self._logger.info,
            "warning": self._logger.warning,
            "error": self._logger.error,
            "critical": self._logger.critical,
        }

        log_func = level_map.get(level.lower(), self._logger.info)
        log_func(message)


# Default logger used across the application
default_logger = Logger()


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured logger instance."""
    return logging.getLogger(name)


def log_exception(logger: logging.Logger, message: str,
                  exc: Exception) -> None:
    """Log ``exc`` with traceback using ``logger``.

    Args:
        logger: Logger instance to use for logging.
        message: Message describing the context of the error.
        exc: The exception object.
    """
    logger.error(message)
    logger.exception(exc)
