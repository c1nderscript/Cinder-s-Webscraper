"""Core scraping engine."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, Optional

import requests

from .content_extractor import ContentExtractor


logger = logging.getLogger(__name__)


class ScraperEngine:
    """Retrieve web pages and extract structured content."""

    def __init__(self, delay: float = 1.0) -> None:
        """Create a ``ScraperEngine``.

        Args:
            delay: Seconds to wait between requests.
        """
        self.delay = delay
        self.session = requests.Session()

    def scrape(self, url: str) -> Optional[Dict[str, Any]]:
        """Scrape the provided URL and return extracted content.

        Args:
            url: The target URL to scrape.

        Returns:
            Optional[Dict[str, Any]]: Extracted data dictionary or ``None`` if
                scraping failed.
        """
        try:
            time.sleep(self.delay)
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            extractor = ContentExtractor()
            return extractor.extract(response.text)
        except requests.RequestException as exc:
            logger.error("Request failed for %s: %s", url, exc)
            return None
        except Exception as exc:  # noqa: BLE001
            logger.error("Unexpected error scraping %s: %s", url, exc)
            return None
