import sys
from pathlib import Path

# Allow importing modules from the src directory when tests are run as a package
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
