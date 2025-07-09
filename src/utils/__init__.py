"""Compatibility wrapper for :mod:`cinder_web_scraper.utils`."""
from importlib import import_module
import sys

_modules = ["config_manager", "file_handler", "logger"]

for mod in _modules:
    target = f"cinder_web_scraper.utils.{mod}"
    sys.modules[f"src.utils.{mod}"] = import_module(target)

__all__ = _modules
