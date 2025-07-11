from __future__ import annotations

from pathlib import Path
from typing import NoReturn

from .logger import default_logger as logger


class FileHandler:
    """High-level helper for file I/O operations."""

    def _log_and_raise(self, message: str, exc: Exception) -> NoReturn:
        logger.error(f"{message}: {exc}")
        raise exc

    def read(self, path: str) -> str:
        """Return the contents of ``path``."""
        try:
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()
            logger.info(f"Read file: {path}")
            return content
        except (FileNotFoundError, PermissionError, OSError) as exc:
            self._log_and_raise(f"Failed to read file {path}", exc)

    def write(self, path: str, data: str) -> None:
        """Write ``data`` to ``path`` creating parent directories when needed."""
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(data)
            logger.info(f"Wrote file: {path}")
        except (PermissionError, OSError) as exc:
            self._log_and_raise(f"Failed to write file {path}", exc)

