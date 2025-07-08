
"""Basic logging utilities built on :mod:`logging`."""

import logging
from pathlib import Path


class Logger:
    """Simple wrapper around :class:`logging.Logger`."""

    def __init__(self, name: str = "cinder.scraper", log_file: str = "data/logs/app.log") -> None:
        """Create a new logger instance.

        Parameters
        ----------
        name:
            Name of the logger to create.
        log_file:
            File path used for the file handler. Directories are created if
            necessary.
        """

        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            Path(log_file).parent.mkdir(parents=True, exist_ok=True)
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )

            file_handler = logging.FileHandler(log_file)
            file_handler.setFormatter(formatter)

            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)

            self.logger.setLevel(logging.INFO)
            self.logger.addHandler(file_handler)
            self.logger.addHandler(stream_handler)

    def log(self, message: str, level: int = logging.INFO) -> None:
        """Log a message with the given severity level."""

        self.logger.log(level, message)


# Default logger used across the application
default_logger = Logger()

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
    """Logger class for application logging."""
    
    def __init__(self, name: str | None = None):
        """Initialize logger with optional name.
        
        Args:
            name: Name for the logger instance.
        """
        self.logger = logging.getLogger(name)
    
    def log(self, message: str, level: str = "info") -> None:
        """Log a message at the specified level.
        
        Args:
            message: The message to log.
            level: The logging level (debug, info, warning, error, critical).
        """
        level_map = {
            "debug": self.logger.debug,
            "info": self.logger.info,
            "warning": self.logger.warning,
            "error": self.logger.error,
            "critical": self.logger.critical,
        }
        
        log_func = level_map.get(level.lower(), self.logger.info)
        log_func(message)


def get_logger(name: str | None = None) -> logging.Logger:
    """Return a configured logger instance."""

    return logging.getLogger(name)


def log_exception(logger: logging.Logger, message: str, exc: Exception) -> None:
    """Log ``exc`` with traceback using ``logger``.

    Args:
        logger: Logger instance to use for logging.
        message: Message describing the context of the error.
        exc: The exception object.
    """

    logger.error(message)
    logger.exception(exc)

