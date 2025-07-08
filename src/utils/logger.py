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

