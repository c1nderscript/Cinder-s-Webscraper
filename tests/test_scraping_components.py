

from unittest.mock import patch
import json


from cinder_web_scraper.scraping.scraper_engine import ScraperEngine
from cinder_web_scraper.scraping.content_extractor import ContentExtractor
from cinder_web_scraper.scraping.output_manager import OutputManager



def test_scraper_engine_scrape():
    engine = ScraperEngine()
    with patch.object(engine.session, "get", side_effect=Exception("fail")):
        assert engine.scrape("https://example.com") is None


def test_content_extractor_extract():
    extractor = ContentExtractor()
    result = extractor.extract("<html></html>")
    assert isinstance(result, dict)

class DummyResponse:
    def __init__(self, text: str, status: int = 200):
        self.text = text
        self.status_code = status

    def raise_for_status(self):
        if not (200 <= self.status_code < 400):
            raise Exception("http error")


def test_scrape_success():
    engine = ScraperEngine(delay=0)
    html = "<html><p>Hello</p></html>"
    with patch.object(engine.session, "get", return_value=DummyResponse(html)) as mock_get, \
         patch("time.sleep") as mock_sleep:
        result = engine.scrape("http://example.com")
        assert result == html
        mock_get.assert_called_once()
        mock_sleep.assert_called_once()


def test_scrape_failure():
    engine = ScraperEngine(delay=0)
    from requests.exceptions import RequestException

    with patch.object(engine.session, "get", side_effect=RequestException("fail")):
        assert engine.scrape("http://bad") is None


def test_extractor_selector():
    html = "<div><p class='x'>A</p><p class='x'>B</p></div>"
    extractor = ContentExtractor()
    result = extractor.extract(html, "p.x")
    assert result == ["A", "B"]



def test_output_manager_save(tmp_path):
    manager = OutputManager()

    assert manager.save({}, str(tmp_path / "out.json")) is True

    path = tmp_path / "out.txt"
    assert manager.save("hello", str(path)) is True
    assert path.read_text(encoding="utf-8") == "hello"
    json_path = tmp_path / "out.json"
    data = {"a": 1}
    assert manager.save(data, str(json_path)) is True
    assert json.loads(json_path.read_text(encoding="utf-8")) == data

