"""Compatibility layer exposing :mod:`cinder_web_scraper` as ``src``."""

from importlib import import_module
import sys
from types import ModuleType

_MODULES = ["utils", "gui", "scraping", "scheduling", "main"]

__all__ = list(_MODULES)

# Preload submodules to allow ``import src.utils`` style imports
for _mod in _MODULES:
    sys.modules[f"src.{_mod}"] = import_module(f"cinder_web_scraper.{_mod}")


def __getattr__(name: str) -> ModuleType:
    """Return the mapped submodule if present."""
    if name in _MODULES:
        return sys.modules[f"src.{name}"]
    raise AttributeError(f"module 'src' has no attribute '{name}'")
