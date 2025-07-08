from src.scraping.scraper_engine import ScraperEngine


def test_scrape_returns_none():
    engine = ScraperEngine()
    result = engine.scrape("http://example.com")
    assert result is None
