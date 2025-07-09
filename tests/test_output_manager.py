import json
import csv
from pathlib import Path

import pytest

from cinder_web_scraper.scraping.output_manager import OutputManager


@pytest.fixture
def manager(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    return OutputManager()


def test_save_json(manager):
    data = {"name": "Alice", "age": 30}
    assert manager.save(data, "data.json") is True
    p = Path("output/data.json")
    assert p.exists()
    with p.open() as f:
        assert json.load(f) == data


def test_save_csv(manager):
    data = [{"name": "A", "val": 1}, {"name": "B", "val": 2}]
    assert manager.save(data, "items.csv") is True
    p = Path("output/items.csv")
    assert p.exists()
    with p.open() as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert rows == [{"name": "A", "val": "1"}, {"name": "B", "val": "2"}]


def test_save_text_nested(manager):
    data = "Hello world"
    assert manager.save(data, "nested/hello.txt") is True
    p = Path("output/nested/hello.txt")
    assert p.exists()
    assert p.read_text() == data
