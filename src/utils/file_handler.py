"""Utility functions for file operations."""

from __future__ import annotations

import os


class FileHandler:
    """High-level helper for reading and writing text files."""

    def read(self, path: str) -> str:
        """Read a file and return its contents.

        Args:
            path: Path to the file to read.

        Returns:
            str: The contents of the file.

        Raises:
            FileNotFoundError: If ``path`` does not exist.
            PermissionError: If the file cannot be read due to permissions.
            OSError: For any other I/O related errors.
        """
        try:
            with open(path, "r", encoding="utf-8") as fh:
                return fh.read()
        except FileNotFoundError:
            raise
        except PermissionError:
            raise
        except OSError as exc:
            raise OSError(f"Failed to read '{path}'") from exc

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
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as fh:
                fh.write(data)
        except PermissionError:
            raise
        except OSError as exc:
            raise OSError(f"Failed to write to '{path}'") from exc
