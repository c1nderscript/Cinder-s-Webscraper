from src.scraping.output_manager import OutputManager


def test_save_returns_none(tmp_path):
    manager = OutputManager()
    data = {"hello": "world"}
    path = tmp_path / "output.txt"
    result = manager.save(data, str(path))
    assert result is None
