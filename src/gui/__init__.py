"""Compatibility wrapper for :mod:`cinder_web_scraper.gui`."""
from importlib import import_module
import sys

_modules = [
    "main_window",
    "website_manager",
    "scheduler_dialog",
    "settings_panel",
]

for mod in _modules:
    target = f"cinder_web_scraper.gui.{mod}"
    sys.modules[f"src.gui.{mod}"] = import_module(target)

__all__ = _modules
