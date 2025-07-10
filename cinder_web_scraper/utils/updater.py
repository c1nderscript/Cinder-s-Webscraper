"""Utilities for updating the local repository."""

from __future__ import annotations

import subprocess

from .logger import get_logger

logger = get_logger(__name__)


def update_repo() -> bool:
    """Run ``git pull`` to update the repository.

    Returns:
        ``True`` if the command succeeds, otherwise ``False``.
    """
    try:
        subprocess.run(
            ["git", "pull"],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info("Repository updated via git pull")
        return True
    except (subprocess.CalledProcessError, OSError) as exc:
        logger.error(f"Git pull failed: {exc}")
        return False
