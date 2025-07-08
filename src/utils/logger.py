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

