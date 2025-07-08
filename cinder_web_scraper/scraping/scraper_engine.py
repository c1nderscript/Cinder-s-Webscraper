"""Core scraping engine using ``requests``."""

from __future__ import annotations

import logging
import time
from typing import Any, Dict, Optional

import requests
from requests import Response
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

from .content_extractor import ContentExtractor
from .output_manager import OutputManager

from src.utils.logger import default_logger as logger

class ScraperEngine:
    """Download pages and extract data using provided helpers with retry support."""

    def __init__(
        self,
        extractor: Optional[ContentExtractor] = None,
        output_manager: Optional[OutputManager] = None,
        config: Optional[Dict[str, Any]] = None,
        delay: float = 1.0,
    ) -> None:
        """Initialize the engine with dependencies and configuration.

        Args:
            extractor: ``ContentExtractor`` instance for parsing HTML.
            output_manager: ``OutputManager`` instance for persisting data.
            config: Optional configuration dictionary. Supported keys are
                ``user_agent``, ``delay``, ``timeout``, and ``retries``.
            delay: Seconds to wait between requests (fallback if not in config).
        """
        self.extractor = extractor or ContentExtractor()
        self.output_manager = output_manager or OutputManager()
        self.config = config or {}

        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": self.config.get("user_agent", "Cinder Web Scraper 1.0")}
        )
        self.delay: float = float(self.config.get("delay", delay))
        self.timeout: int = int(self.config.get("timeout", 30))
        self.retries: int = int(self.config.get("retries", 3))

    def scrape(self, url: str, output_path: Optional[str] = None) -> Optional[str]:
        """Scrape ``url`` and return the HTML content with retry support.

        The method respects the configured request delay and handles common
        network errors gracefully. If output_path is provided, extracted data
        is also saved.

        Args:
            url: The target URL to scrape.
            output_path: Optional file path where extracted content should be saved.

        Returns:
            The raw HTML on success, otherwise ``None``.
        """
        for attempt in range(1, self.retries + 1):
            try:
                logger.log(f"Scraping URL: {url} (attempt {attempt})")
                time.sleep(self.delay)

                response: Response = self.session.get(url, timeout=self.timeout)
                response.raise_for_status()

                # If output_path is provided, extract and save data
                if output_path:
                    data = self._extract_data(response.text)
                    self.output_manager.save(data, output_path)

                return response.text

            except RequestException as exc:
                logger.error(f"Request failed for {url} (attempt {attempt}): {exc}")
                if attempt == self.retries:
                    return None
            except Exception as exc:  # pylint: disable=broad-except
                logger.error(f"Unexpected error scraping {url}: {exc}")
                return None

        return None

    def _extract_data(self, html: str) -> Any:
        """Parse ``html`` content and delegate extraction."""
        soup = BeautifulSoup(html, "html.parser")
        return self.extractor.extract(str(soup))
