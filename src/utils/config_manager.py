"""Utility functions for reading and writing configuration files."""

import json
import os
from typing import Any, Dict

from .logger import default_logger as logger

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
            config = json.load(fp)
        logger.log(f"Loaded configuration from {path}")
        return config
    except FileNotFoundError:
        logger.log(f"Configuration file not found: {path}")
        # Return a copy of the default configuration if the file is missing
        return DEFAULT_CONFIG.copy()
    except json.JSONDecodeError:
        logger.log(f"Invalid JSON in configuration: {path}")
        # Invalid JSON content; ignore the file and return defaults
        return DEFAULT_CONFIG.copy()
    except OSError as exc:
        logger.log(f"Error reading configuration {path}: {exc}")
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
        logger.log(f"Saved configuration to {path}")
        return True
    except OSError as exc:
        logger.log(f"Failed to save configuration to {path}: {exc}")
        return False
