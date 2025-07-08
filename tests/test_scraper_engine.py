from src.scraping.scraper_engine import ScraperEngine


def test_scraper_engine_scrape_returns_content():
    """Test that scraper engine can successfully fetch content."""
    engine = ScraperEngine()
    result = engine.scrape('http://example.com')
    # Should return HTML content, not None, for a valid URL
    assert result is not None
    assert isinstance(result, str)
    assert 'Example Domain' in result  # example.com contains this text


def test_scraper_engine_scrape_returns_none_for_invalid_url():
    """Test that scraper engine returns None for invalid URLs."""
    engine = ScraperEngine()
    result = engine.scrape('http://invalid-url-that-does-not-exist-12345.com')
    # Should return None for invalid URLs
    assert result is None
