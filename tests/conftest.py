import sys
from pathlib import Path

# Ensure the package directory is on sys.path for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "cinder_web_scraper"))
