"""Utility helpers for reading and writing text files."""

from pathlib import Path
from typing import NoReturn

from .logger import default_logger as logger


class FileHandler:
    """High-level helper for file I/O operations."""

    def _log_and_raise(self, message: str, exc: Exception) -> NoReturn:
        """Log ``exc`` using ``message`` and re-raise it.

        Args:
            message: Description of the failure.
            exc: The caught exception.
        """
        logger.error(f"{message}: {exc}")
        raise exc


    def read(self, path: str) -> str:
        """Return the contents of ``path``."""
        try:
            with open(path, "r", encoding="utf-8") as fp:
                content = fp.read()
            logger.log(f"Read file: {path}")
            return content


        except (FileNotFoundError, PermissionError, OSError) as exc:
            logger.error(f"Failed to read file {path}: {exc}")


        except (FileNotFoundError, PermissionError, OSError) as exc:
            self._log_and_raise(f"Failed to read file {path}", exc)


        except (FileNotFoundError, PermissionError, OSError) as exc:
            logger.log(f"Failed to read file {path}: {exc}")

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
        """Write ``data`` to ``path`` creating parent directories when needed."""
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, "w", encoding="utf-8") as fp:
                fp.write(data)
            logger.info(f"Wrote file: {path}")
        except (PermissionError, OSError) as exc:
            logger.error(f"Failed to write file {path}: {exc}")

                
            logger.info(f"Wrote file: {path}")
        except (PermissionError, OSError) as exc:
            self._log_and_raise(f"Failed to write file {path}", exc)

            logger.log(f"Wrote file: {path}")
        except (PermissionError, OSError) as exc:
            logger.log(f"Failed to write file {path}: {exc}")

            logger.info(f"Wrote file: {path}")
        except PermissionError as exc:
            logger.error(f"Permission denied writing {path}: {exc}")
            raise

        except OSError as exc:
            logger.error(f"Failed to write file {path}: {exc}")







        except (PermissionError, OSError) as exc:
            logger.log(f"Failed to write file {path}: {exc}")






            raise



            raise
