from src.scraping.scraper_engine import ScraperEngine


def test_scraper_engine_scrape_returns_html():
    engine = ScraperEngine()
    assert isinstance(engine.scrape('http://example.com'), str)

def test_scraper_engine_scrape_working_url():
    engine = ScraperEngine()
    content = engine.scrape('http://example.com')
    assert '<html>' in content 
    assert '<title>Example Domain</title>' in content
