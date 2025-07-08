"""Manage websites to be scraped."""

from __future__ import annotations

from typing import List


class WebsiteManager:
    """Manage website configuration logic."""

    def __init__(self) -> None:
        self.websites: List[str] = []

    def add_website(self, url: str) -> None:
        """Add a website to the list of sites to scrape."""

        if url not in self.websites:
            self.websites.append(url)

    def remove_website(self, url: str) -> None:
        """Remove a website from the scrape list."""

        if url in self.websites:
            self.websites.remove(url)
