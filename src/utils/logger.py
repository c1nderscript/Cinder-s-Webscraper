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
