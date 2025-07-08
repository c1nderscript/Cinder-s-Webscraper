"""Handle output of scraped data."""

from __future__ import annotations

import json
import logging
from pathlib import Path
from typing import Any


logger = logging.getLogger(__name__)


class OutputManager:
    """Save scraped data to files in various formats."""

    def save(self, data: Any, path: str) -> bool:
        """Save scraped data to a file path.

        Args:
            data: Parsed data to persist. Dictionaries and lists are stored as
                JSON; other types are converted to strings.
            path: Destination file path.

        Returns:
            bool: ``True`` if the data was saved successfully, ``False``
                otherwise.
        """
        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            if isinstance(data, (dict, list)):
                with open(path, "w", encoding="utf-8") as fp:
                    json.dump(data, fp, indent=4)
            else:
                with open(path, "w", encoding="utf-8") as fp:
                    fp.write(str(data))
            return True
        except OSError as exc:
            logger.error("Failed to save output to %s: %s", path, exc)
            return False
