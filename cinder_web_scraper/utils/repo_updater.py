"""Utilities for updating the local git repository."""

from __future__ import annotations

import subprocess

from .logger import default_logger as logger


def update_repo() -> bool:
    """Run ``git pull`` to update the repository.

    Returns:
        ``True`` if the command succeeded, otherwise ``False``.
    """
    try:
        result = subprocess.run(
            ["git", "pull"], capture_output=True, text=True, check=False
        )
        if result.returncode == 0:
            logger.info("Repository updated successfully")
            return True
        logger.error(f"Failed to update repository: {result.stderr.strip()}")
        return False
    except Exception as exc:  # pragma: no cover - unexpected subprocess errors
        logger.error(f"Error running git pull: {exc}")
        return False
