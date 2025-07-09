"""Handle output of scraped data."""

from __future__ import annotations

import csv
import json
import os
from pathlib import Path
from typing import Any

from src.utils.logger import default_logger as logger


class OutputManager:
    """Persist scraped data to files inside the ``output`` directory."""

    BASE_DIR = Path("output")

    def save(self, data: Any, path: str) -> bool:
        """Save scraped ``data`` to ``path``.

        The output format is determined from the file extension. Supported
        extensions are ``.csv``, ``.json`` and ``.txt`` (or any other extension
        for plain text).  ``path`` is created relative to the ``output``
        directory if it is not an absolute path.  All necessary directories are
        created automatically.

        Args:
            data: Parsed data to persist. ``data`` should be a sequence of
                dictionaries for CSV output, any JSON serialisable object for
                JSON output and a string or sequence of strings for plain text
                output.
            path: Destination file path or name.

        Returns:
            bool: ``True`` if the file was written successfully, ``False``
            otherwise.
        """

        logger.log(f"Saving data to {path}")
        # Actual saving logic would go here


        dest = Path(path)
        if not dest.is_absolute():
            dest = self.BASE_DIR / dest

        try:
            dest.parent.mkdir(parents=True, exist_ok=True)
            ext = dest.suffix.lower()
            if ext == ".json":
                with dest.open("w", encoding="utf-8") as fp:
                    json.dump(data, fp, indent=4)
            elif ext == ".csv":
                with dest.open("w", newline="", encoding="utf-8") as fp:
                    if (
                        isinstance(data, list)
                        and data
                        and isinstance(data[0], dict)
                    ):
                        writer = csv.DictWriter(fp, fieldnames=data[0].keys())
                        writer.writeheader()
                        writer.writerows(data)
                    else:
                        writer = csv.writer(fp)
                        if isinstance(data, list):
                            writer.writerows(data)
                        else:
                            writer.writerow([data])
            else:
                with dest.open("w", encoding="utf-8") as fp:
                    if isinstance(data, list):
                        fp.write("\n".join(str(item) for item in data))
                    else:
                        fp.write(str(data))
            return True
        except OSError:
            return False

