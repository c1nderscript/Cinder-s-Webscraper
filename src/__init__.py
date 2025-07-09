"""Compatibility layer mapping the legacy ``src`` namespace to ``cinder_web_scraper``."""

import sys
from importlib import import_module

PACKAGE = "cinder_web_scraper"

# Map submodules to maintain backward compatibility with the old ``src``
# namespace. Import ``utils`` first as other modules depend on it.
for _mod in ["utils", "scheduling", "scraping", "gui", "main"]:
    sys.modules[f"src.{_mod}"] = import_module(f"{PACKAGE}.{_mod}")
