import json
import os
from typing import Any, Dict

# Default configuration used when loading fails or no file is found
DEFAULT_CONFIG: Dict[str, Any] = {
    "websites": [],
    "settings": {}
}

def load_config(path: str) -> Dict[str, Any]:
    """Load configuration from ``path`` in JSON format.

    If the file does not exist or contains invalid JSON, ``DEFAULT_CONFIG`` is
    returned instead.
    """
    try:
        with open(path, "r", encoding="utf-8") as fp:
            return json.load(fp)
    except FileNotFoundError:
        # Return a copy of the default configuration if the file is missing
        return DEFAULT_CONFIG.copy()
    except json.JSONDecodeError:
        # Invalid JSON content; ignore the file and return defaults
        return DEFAULT_CONFIG.copy()
    except OSError:
        # Any other file-related error also results in default config
        return DEFAULT_CONFIG.copy()

def save_config(data: Dict[str, Any], path: str) -> bool:
    """Save ``data`` as JSON to ``path``.

    The directory is created if it does not exist. Returns ``True`` if the
    configuration was saved successfully, otherwise ``False``.
    """
    try:
        os.makedirs(os.path.dirname(path) or '.', exist_ok=True)
        with open(path, "w", encoding="utf-8") as fp:
            json.dump(data, fp, indent=4)
        return True
    except OSError:
        return False
