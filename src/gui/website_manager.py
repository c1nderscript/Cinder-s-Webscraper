"""Manage websites to be scraped."""


class WebsiteManager:
    """Manage website configuration logic."""

    def add_website(self, url: str) -> None:
        """Add a website to the list of sites to scrape.

        Args:
            url: The URL of the website to add.

        Returns:
            None: This method does not return anything.
        """
        pass

    def remove_website(self, url: str) -> None:
        """Remove a website from the scrape list.

        Args:
            url: The URL of the website to remove.

        Returns:
            None: This method does not return anything.
        """
        pass
