"""Utility functions for file operations."""


from pathlib import Path

from .logger import default_logger as logger


class FileHandler:
    """Utility wrapper around standard file operations."""

    def read(self, path: str) -> str:
        """Read a file and return its contents.

        Args:
            path: Path to the file to read.

        Returns:
            str: The contents of the file.
        """
        try:
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()
            logger.log(f"Read file: {path}")
            return content
        except OSError as exc:
            logger.log(f"Failed to read file {path}: {exc}")
            raise

    def write(self, path: str, data: str) -> None:
        """Write ``data`` to ``path``.

        Args:
            path: Destination file path.
            data: Text data to write.

        Returns:
            None: This method does not return anything.
        """
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(data)
            logger.log(f"Wrote file: {path}")
        except OSError as exc:
            logger.log(f"Failed to write file {path}: {exc}")
            raise
