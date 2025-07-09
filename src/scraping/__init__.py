"""Compatibility wrapper for :mod:`cinder_web_scraper.scraping`."""
from importlib import import_module
import sys

_modules = ["content_extractor", "output_manager", "scraper_engine"]

for mod in _modules:
    target = f"cinder_web_scraper.scraping.{mod}"
    sys.modules[f"src.scraping.{mod}"] = import_module(target)

__all__ = _modules
