"""Compatibility wrapper for :mod:`cinder_web_scraper.scheduling`."""
from importlib import import_module
import sys

_modules = ["schedule_manager", "task_scheduler"]

for mod in _modules:
    target = f"cinder_web_scraper.scheduling.{mod}"
    sys.modules[f"src.scheduling.{mod}"] = import_module(target)

__all__ = _modules
