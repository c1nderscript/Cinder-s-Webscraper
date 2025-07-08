from src.scraping.scraper_engine import ScraperEngine


def test_scraper_engine_scrape_returns_none():
    engine = ScraperEngine()
    assert engine.scrape('http://example.com') is None
