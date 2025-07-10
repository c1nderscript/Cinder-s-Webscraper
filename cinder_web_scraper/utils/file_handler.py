"""Utility functions for file operations."""

from __future__ import annotations

from pathlib import Path

from .logger import default_logger as logger


class FileHandler:
    """High-level helper for reading and writing text files."""

    def read(self, path: str) -> str:
        """Return the contents of ``path``.

        Args:
            path: Path to the file to read.

        Returns:
            The contents of the file.

        Raises:
            FileNotFoundError: If ``path`` does not exist.
            PermissionError: If the file cannot be read due to permissions.
            OSError: For any other I/O related errors.
        """
        try:
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()
            logger.info(f"Read file: {path}")
            return content

        except FileNotFoundError:
            logger.error(f"File not found: {path}")
            raise
        except PermissionError as exc:
            logger.error(f"Permission denied reading {path}: {exc}")
            raise
        except OSError as exc:
            logger.error(f"Failed to read file {path}: {exc}")
            raise


    def write(self, path: str, data: str) -> None:
        """Write ``data`` to ``path``.

        The target directory is created automatically if it does not exist.

        Args:
            path: Destination file path.
            data: Text data to write.

        Raises:
            PermissionError: If the file cannot be written due to permissions.
            OSError: For any other I/O related errors.
        """
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(data)

            logger.info(f"Wrote file: {path}")
        except PermissionError as exc:
            logger.error(f"Permission denied writing {path}: {exc}")
            raise
        except OSError as exc:
            logger.error(f"Failed to write file {path}: {exc}")
            raise

