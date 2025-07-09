"""Compatibility shim mapping ``src`` package to :mod:`cinder_web_scraper`."""

from importlib import import_module
import sys

_subpackages = {"gui", "scheduling", "scraping", "utils"}


def __getattr__(name: str):
    if name in _subpackages:
        module = import_module(f"cinder_web_scraper.{name}")
        sys.modules[f"src.{name}"] = module
        return module
    raise AttributeError(f"module 'src' has no attribute {name}")

__all__ = list(_subpackages)
