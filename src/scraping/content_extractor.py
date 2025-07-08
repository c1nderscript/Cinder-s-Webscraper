"""Extract content from scraped pages using ``BeautifulSoup``."""

from __future__ import annotations

from typing import List, Optional

from bs4 import BeautifulSoup


class ContentExtractor:
    """Parse HTML and return text from selected elements."""

    def extract(self, html: str, selector: Optional[str] = None) -> List[str]:
        """Extract information from ``html``.

        Args:
            html: Raw HTML string to parse.
            selector: Optional CSS selector. When provided, text from matching
                elements is returned; otherwise the entire page text is
                returned.

        Returns:
            A list of text strings extracted from the HTML.
        """

        soup = BeautifulSoup(html, "html.parser")
        if selector:
            elements = soup.select(selector)
            return [element.get_text(strip=True) for element in elements]
        return [soup.get_text(strip=True)]
