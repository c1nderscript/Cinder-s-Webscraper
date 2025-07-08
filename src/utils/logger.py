"""Application-wide logging utilities.

This module configures the standard Python ``logging`` module to log messages
both to the console and to a log file located in ``data/logs/``. Other modules
can retrieve loggers using :func:`get_logger` and log messages as needed.
"""

from __future__ import annotations

import logging
from pathlib import Path
from typing import Optional

# Default log file path relative to the project root
LOG_FILE_PATH = Path("data/logs/scraper.log")

# Internal flag to avoid reconfiguring logging multiple times
_CONFIGURED = False


def configure(log_file: Optional[Path] = None) -> None:
    """Configure the logging system.

    Parameters
    ----------
    log_file : Optional[Path]
        Optional path to the log file. If ``None``, ``LOG_FILE_PATH`` is used.

    Returns
    -------
    None
    """
    global _CONFIGURED
    if _CONFIGURED:
        return

    path = log_file or LOG_FILE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(path),
            logging.StreamHandler(),
        ],
    )

    _CONFIGURED = True


# Automatically configure logging when the module is imported
configure()

# Default logger for this module
_logger = logging.getLogger(__name__)


def get_logger(name: str) -> logging.Logger:
    """Return a logger with the specified ``name``.

    Parameters
    ----------
    name : str
        Name of the logger to retrieve.

    Returns
    -------
    logging.Logger
        Configured logger instance.
    """
    return logging.getLogger(name)


def info(message: str) -> None:
    """Log an info level ``message`` using the module logger."""
    _logger.info(message)


def warning(message: str) -> None:
    """Log a warning level ``message`` using the module logger."""
    _logger.warning(message)


def error(message: str) -> None:
    """Log an error level ``message`` using the module logger."""
    _logger.error(message)
