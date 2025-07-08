import pytest
from src.scraping.content_extractor import ContentExtractor


def test_basic_html():
    html = (
        "<html><head><title>Test Page</title></head>"
        "<body><p>Hello</p><a href='http://example.com'>Link</a>"
        "<img src='image.jpg'/></body></html>"
    )
    extractor = ContentExtractor()
    result = extractor.extract(html)
    assert result["title"] == "Test Page"
    assert result["links"] == ["http://example.com"]
    assert result["images"] == ["image.jpg"]
    assert result["text"] == "Hello Link"


def test_missing_elements():
    html = "<html><body><p>No links or images here</p></body></html>"
    extractor = ContentExtractor()
    result = extractor.extract(html)
    assert result["title"] is None
    assert result["links"] == []
    assert result["images"] == []
    assert result["text"] == "No links or images here"


def test_empty_html():
    extractor = ContentExtractor()
    result = extractor.extract("")
    assert result["title"] is None
    assert result["links"] == []
    assert result["images"] == []
    assert result["text"] == ""
