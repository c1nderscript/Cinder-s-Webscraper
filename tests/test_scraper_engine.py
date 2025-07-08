import requests
from unittest.mock import patch

from bs4 import BeautifulSoup

from src.scraping.scraper_engine import ScraperEngine
from src.scraping.content_extractor import ContentExtractor
from src.scraping.output_manager import OutputManager


class DummyExtractor(ContentExtractor):
    def extract(self, html: str):
        soup = BeautifulSoup(html, "html.parser")
        title = soup.title.string if soup.title else ""
        return {"title": title}


class DummyOutput(OutputManager):
    def __init__(self):
        self.data = None
        self.path = None

    def save(self, data, path):
        self.data = data
        self.path = path


def test_scrape_success(tmp_path):
    extractor = DummyExtractor()
    output = DummyOutput()
    engine = ScraperEngine(extractor, output, {"delay": 0, "retries": 1})

    html = "<html><head><title>Example</title></head></html>"
    response = requests.Response()
    response.status_code = 200
    response._content = html.encode()

    with patch.object(engine.session, "get", return_value=response) as mock_get:
        data = engine.scrape("http://example.com", str(tmp_path / "out.json"))

    assert mock_get.called
    assert data == {"title": "Example"}
    assert output.data == {"title": "Example"}


def test_scrape_retries(tmp_path):
    extractor = DummyExtractor()
    output = DummyOutput()
    engine = ScraperEngine(extractor, output, {"delay": 0, "retries": 2})

    with patch.object(
        engine.session, "get", side_effect=requests.RequestException
    ) as mock_get:
        data = engine.scrape("http://example.com", str(tmp_path / "out.json"))

    assert data is None
    # ensure two attempts were made
    assert mock_get.call_count == 2
    assert output.data is None
