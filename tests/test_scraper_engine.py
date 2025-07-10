import requests
from unittest.mock import patch

from bs4 import BeautifulSoup

from cinder_web_scraper.scraping.scraper_engine import ScraperEngine
from cinder_web_scraper.scraping.content_extractor import ContentExtractor
from cinder_web_scraper.scraping.output_manager import OutputManager


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
        return True


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
    assert data == html
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


def test_scraper_engine_scrape_returns_content():
    """Test that scraper engine can successfully fetch content."""
    engine = ScraperEngine(delay=0)
    html = "<html><head><title>Example Domain</title></head><body></body></html>"
    response = requests.Response()
    response.status_code = 200
    response._content = html.encode()

    with patch.object(engine.session, "get", return_value=response) as mock_get, \
         patch("time.sleep"):
        result = engine.scrape('http://example.com')

    mock_get.assert_called_once()
    # Should return HTML content, not None, for a valid URL
    assert result is not None
    assert isinstance(result, str)
    assert 'Example Domain' in result


def test_scraper_engine_scrape_returns_none_for_invalid_url():
    """Test that scraper engine returns None for invalid URLs."""
    engine = ScraperEngine(delay=0, config={"retries": 1})
    with patch.object(engine.session, "get", side_effect=requests.RequestException) as mock_get, \
         patch("time.sleep"):
        result = engine.scrape('http://invalid-url-that-does-not-exist-12345.com')

    mock_get.assert_called_once()
    # Should return None for invalid URLs
    assert result is None


def test_scraper_engine_scrape_working_url():
    engine = ScraperEngine(delay=0)
    html = "<html><head><title>Example Domain</title></head><body></body></html>"
    response = requests.Response()
    response.status_code = 200
    response._content = html.encode()

    with patch.object(engine.session, "get", return_value=response) as mock_get, \
         patch("time.sleep"):
        content = engine.scrape('http://example.com')

    mock_get.assert_called_once()
    assert '<html>' in content
    assert '<title>Example Domain</title>' in content
