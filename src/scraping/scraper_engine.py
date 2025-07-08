"""Core scraping engine."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, Optional

import requests
from bs4 import BeautifulSoup

from .content_extractor import ContentExtractor
from .output_manager import OutputManager

logger = logging.getLogger(__name__)


class ScraperEngine:
    """Download pages and extract data using provided helpers."""

    def __init__(
        self,
        extractor: ContentExtractor,
        output_manager: OutputManager,
        config: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Initialize the engine with dependencies and configuration.

        Args:
            extractor: ``ContentExtractor`` instance for parsing HTML.
            output_manager: ``OutputManager`` instance for persisting data.
            config: Optional configuration dictionary. Supported keys are
                ``user_agent``, ``delay``, ``timeout``, and ``retries``.
        """

        self.extractor = extractor
        self.output_manager = output_manager
        self.config = config or {}

        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": self.config.get("user_agent", "Cinder Web Scraper 1.0")}
        )
        self.delay: float = float(self.config.get("delay", 1))
        self.timeout: int = int(self.config.get("timeout", 30))
        self.retries: int = int(self.config.get("retries", 3))

    def scrape(self, url: str, output_path: str) -> Optional[Any]:
        """Scrape ``url`` and store parsed results.

        Args:
            url: The target URL to scrape.
            output_path: File path where extracted content should be saved.

        Returns:
            Parsed data from the extractor, or ``None`` if scraping fails.
        """

        for attempt in range(1, self.retries + 1):
            try:
                time.sleep(self.delay)

                response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()

                data = self._extract_data(response.text)
                self.output_manager.save(data, output_path)
                return data

            except requests.RequestException as exc:  # noqa: E501 - long error string
                logger.error("Request failed for %s (attempt %s): %s", url, attempt, exc)
                if attempt == self.retries:
                    return None
            except Exception as exc:  # pylint: disable=broad-except
                logger.error("Unexpected error scraping %s: %s", url, exc)
                return None

        return None

    def _extract_data(self, html: str) -> Any:
        """Parse ``html`` content and delegate extraction."""

        soup = BeautifulSoup(html, "html.parser")
        return self.extractor.extract(str(soup))

