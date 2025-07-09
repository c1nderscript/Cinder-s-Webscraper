
"""Compatibility layer exposing :mod:`cinder_web_scraper` as ``src``."""
from importlib import import_module
import sys

_MODULES = ["utils", "gui", "scraping", "scheduling", "main"]

__all__ = list(_MODULES)


def __getattr__(name: str):
    if name in _MODULES:
        module = import_module(f"cinder_web_scraper.{name}")
        sys.modules[f"src.{name}"] = module
        return module
    raise AttributeError(f"module 'src' has no attribute '{name}'")

"""Compatibility layer mapping the legacy ``src`` namespace to ``cinder_web_scraper``."""

import sys
from importlib import import_module

PACKAGE = "cinder_web_scraper"

# Map submodules to maintain backward compatibility with the old ``src``
# namespace. Import ``utils`` first as other modules depend on it.
for _mod in ["utils", "scheduling", "scraping", "gui", "main"]:
    sys.modules[f"src.{_mod}"] = import_module(f"{PACKAGE}.{_mod}")
