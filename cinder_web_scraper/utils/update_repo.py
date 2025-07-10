from __future__ import annotations

"""Utility to update the local repository using ``git pull``."""

import subprocess
from typing import List

from .logger import get_logger, log_exception

logger = get_logger(__name__)


def update_repo(remote: str = "origin") -> str:
    """Run ``git pull`` for the given ``remote``.

    Parameters
    ----------
    remote:
        Name of the git remote to pull from.

    Returns
    -------
    str
        The stdout from the ``git pull`` command.

    Raises
    ------
    RuntimeError
        If ``git pull`` exits with a non-zero status.
    """
    try:
        result = subprocess.run(
            ["git", "pull", remote],
            capture_output=True,
            text=True,
            check=True,
        )
        output = result.stdout.strip()
        if result.stderr:
            logger.warning(result.stderr.strip())
        logger.info("Repository updated from %s", remote)
        return output
    except subprocess.CalledProcessError as exc:  # pragma: no cover - subprocess errors
        log_exception(logger, f"Failed to update repository from {remote}", exc)
        raise RuntimeError(exc.stderr.strip() or "git pull failed") from exc
