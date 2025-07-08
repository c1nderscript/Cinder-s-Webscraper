"""Handle output of scraped data."""

from __future__ import annotations

import json
import os
from typing import Any


class OutputManager:
    """Persist scraped data to disk."""

    def save(self, data: Any, path: str) -> bool:
        """Save ``data`` to ``path``.

        The directory is created if necessary. ``dict`` and ``list`` instances
        are serialized as JSON while other data types are written as plain text.

        Args:
            data: Parsed data to persist.
            path: Destination file path.

        Returns:
            ``True`` if the operation succeeds, otherwise ``False``.
        """

        try:
            os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
            with open(path, "w", encoding="utf-8") as f:
                if isinstance(data, (dict, list)):
                    json.dump(data, f, indent=2)
                else:
                    f.write(str(data))
            return True
        except OSError:
            return False
