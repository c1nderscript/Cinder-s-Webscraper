"""Utility functions for file operations."""

from __future__ import annotations

import logging
from pathlib import Path


logger = logging.getLogger(__name__)


class FileHandler:
    """Provide simple file reading and writing helpers."""

    def read(self, path: str) -> str:
        """Read a file and return its contents.

        Args:
            path: Path to the file to read.

        Returns:
            str: The contents of the file. Empty string if an error occurs.
        """
        try:
            with open(path, "r", encoding="utf-8") as fp:
                return fp.read()
        except FileNotFoundError:
            logger.error("File not found: %s", path)
            return ""
        except OSError as exc:
            logger.error("Failed to read %s: %s", path, exc)
            return ""

    def write(self, path: str, data: str) -> bool:
        """Write ``data`` to ``path``.

        Args:
            path: Destination file path.
            data: Text data to write.

        Returns:
            bool: ``True`` if the write succeeded, ``False`` otherwise.
        """
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(data)
            return True
        except OSError as exc:
            logger.error("Failed to write %s: %s", path, exc)
            return False
