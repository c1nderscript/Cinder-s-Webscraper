
"""Backward compatibility package exposing :mod:`cinder_web_scraper` as ``src``.

This allows legacy imports such as ``import src.gui`` to resolve to the
corresponding modules in :mod:`cinder_web_scraper`.
"""

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
