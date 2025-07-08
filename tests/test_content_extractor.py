from src.scraping.content_extractor import ContentExtractor


def test_extract_returns_none():
    extractor = ContentExtractor()
    html = "<html><body><p>Hello</p></body></html>"
    result = extractor.extract(html)
    assert result is None
