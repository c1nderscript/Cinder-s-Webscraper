from src.utils.file_handler import FileHandler
from src.utils.logger import Logger
from src.scraping.content_extractor import ContentExtractor
from src.scraping.scraper_engine import ScraperEngine
from src.scraping.output_manager import OutputManager
from src.gui.website_manager import WebsiteManager

import json
import requests


def test_file_handler_read_write(tmp_path):
    handler = FileHandler()
    path = tmp_path / "file.txt"
    assert handler.write(str(path), "hello") is True
    assert handler.read(str(path)) == "hello"


def test_file_handler_read_missing(tmp_path):
    handler = FileHandler()
    assert handler.read(str(tmp_path / "missing.txt")) == ""


def test_logger_log(tmp_path):
    log_path = tmp_path / "log.txt"
    logger = Logger(__name__, log_file=str(log_path))
    logger.log("entry")
    assert "entry" in log_path.read_text()


def test_content_extractor():
    html = "<html><head><title>Title</title></head><body><p>A</p><p>B</p></body></html>"
    extractor = ContentExtractor()
    result = extractor.extract(html)
    assert result["title"] == "Title"
    assert result["paragraphs"] == ["A", "B"]


class DummyResponse:
    def __init__(self, text: str, status_code: int = 200) -> None:
        self.text = text
        self.status_code = status_code

    def raise_for_status(self) -> None:
        pass


def test_scraper_engine_scrape(monkeypatch):
    html = "<html><head><title>Title</title></head><body><p>A</p></body></html>"

    def fake_get(self, url, timeout):
        return DummyResponse(html)

    monkeypatch.setattr(requests.Session, "get", fake_get)
    engine = ScraperEngine(delay=0)
    result = engine.scrape("http://example.com")
    assert result and result["title"] == "Title"


def test_output_manager_save(tmp_path):
    manager = OutputManager()
    path = tmp_path / "data.json"
    data = {"k": 1}
    assert manager.save(data, str(path)) is True
    assert json.loads(path.read_text()) == data


def test_website_manager_add_remove():
    manager = WebsiteManager()
    manager.add_website("http://example.com")
    assert "http://example.com" in manager.websites
    manager.remove_website("http://example.com")
    assert "http://example.com" not in manager.websites
