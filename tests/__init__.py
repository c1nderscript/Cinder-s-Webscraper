import sys
from pathlib import Path

# Allow importing modules from the package directory when tests are run as a package
package_path = Path(__file__).resolve().parents[1] / "cinder_web_scraper"
sys.path.insert(0, str(package_path))

# Alias the deprecated ``src`` package name to the actual package so that
# modules using the old imports can still be loaded by the tests.
import cinder_web_scraper
sys.modules.setdefault("src", cinder_web_scraper)
