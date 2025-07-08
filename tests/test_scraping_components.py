from src.scraping.scraper_engine import ScraperEngine
from src.scraping.content_extractor import ContentExtractor
from src.scraping.output_manager import OutputManager


def test_scraper_engine_scrape():
    engine = ScraperEngine()
    assert engine.scrape("https://example.com") is None


def test_content_extractor_extract():
    extractor = ContentExtractor()
    assert extractor.extract("<html></html>") is None


def test_output_manager_save(tmp_path):
    manager = OutputManager()
    assert manager.save({}, str(tmp_path / "out.json")) is None
