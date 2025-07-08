"""Extract content from scraped HTML pages."""

from typing import Any, Dict, List, Optional

from bs4 import BeautifulSoup


class ContentExtractor:
    """Parse HTML and return structured data."""

    def extract(self, html: str) -> Dict[str, Any]:
        """Extract information from HTML content.

        This method parses ``html`` using ``BeautifulSoup`` and returns a
        dictionary containing the page title, all link URLs, image sources and
        the visible text.

        Args:
            html: Raw HTML string to parse.

        Returns:
            Dict[str, Any]: A mapping with the following keys:
                ``title`` (Optional[str]): The contents of the ``<title>`` tag if
                    present, otherwise ``None``.
                ``links`` (List[str]): All ``href`` attributes from ``<a>`` tags.
                ``images`` (List[str]): All ``src`` attributes from ``<img>`` tags.
                ``text`` (str): Visible text extracted from the ``<body>``
                    element, or the entire document if no body exists.
        """

        soup = BeautifulSoup(html, "html.parser")

        title: Optional[str] = None
        if soup.title and soup.title.string:
            title = soup.title.string.strip()

        links: List[str] = [a["href"] for a in soup.find_all("a") if a.get("href")]
        images: List[str] = [img["src"] for img in soup.find_all("img") if img.get("src")]

        if soup.body:
            text = soup.body.get_text(separator=" ", strip=True)
        else:
            text = soup.get_text(separator=" ", strip=True)

        return {
            "title": title,
            "links": links,
            "images": images,
            "text": text,
        }
