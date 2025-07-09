"""Compatibility package mapping to :mod:`cinder_web_scraper`."""
import importlib
import sys

_pkg = "cinder_web_scraper"
# Import utilities first so other subpackages using `src.utils` resolve correctly
_subpackages = ["utils", "gui", "scheduling", "scraping"]

for sub in _subpackages:
    module = importlib.import_module(f"{_pkg}.{sub}")
    sys.modules[f"src.{sub}"] = module

