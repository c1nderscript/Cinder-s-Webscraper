"""Extract content from scraped pages."""

from __future__ import annotations

import logging
from typing import Any, Dict, List

from bs4 import BeautifulSoup


logger = logging.getLogger(__name__)


class ContentExtractor:
    """Parse HTML and return a simple data structure."""

    def extract(self, html: str) -> Dict[str, Any]:
        """Extract information from HTML content.

        Args:
            html: Raw HTML string to parse.

        Returns:
            Dict[str, Any]: Dictionary containing the page title and a list of
                paragraph texts.
        """
        try:
            soup = BeautifulSoup(html, "html.parser")
            title = soup.title.string.strip() if soup.title else ""
            paragraphs: List[str] = [
                p.get_text(strip=True) for p in soup.find_all("p")
            ]
            return {"title": title, "paragraphs": paragraphs}
        except Exception as exc:  # noqa: BLE001
            logger.error("Failed to parse HTML: %s", exc)
            return {"title": "", "paragraphs": []}
