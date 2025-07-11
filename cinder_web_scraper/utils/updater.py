"""Utilities for updating the application from a Git repository."""

from __future__ import annotations

import subprocess
from typing import Tuple

from .logger import get_logger

logger = get_logger(__name__)


def update_repo(remote: str = "origin") -> bool:
    """Run ``git pull`` to update the repository.

    Parameters
    ----------
    remote:
        Name of the git remote to pull from.

    Returns
    -------
    bool
        ``True`` if the command succeeds, otherwise ``False``.
    """
    try:
        subprocess.run(
            ["git", "pull", remote],
            check=True,
            capture_output=True,
            text=True,
        )
        logger.info("Repository updated via git pull")
        return True
    except (subprocess.CalledProcessError, OSError) as exc:
        logger.error("Git pull failed: %s", exc)
        return False


def update_application() -> Tuple[bool, str]:
    """Update the application by pulling the latest changes.

    Returns
    -------
    tuple
        A ``(success, message)`` pair indicating whether the update
        succeeded and providing the command output or error message.
    """
    try:
        result = subprocess.run(
            ["git", "pull", "--ff-only"],
            capture_output=True,
            text=True,
            check=True,
        )
        logger.info("Application updated successfully")
        return True, result.stdout.strip()
    except subprocess.CalledProcessError as exc:
        msg = exc.stderr.strip() if exc.stderr else str(exc)
        logger.error("Git pull failed: %s", msg)
        return False, msg
    except OSError as exc:  # Network or OS issues
        logger.error("Failed to run git pull: %s", exc)
        return False, str(exc)
