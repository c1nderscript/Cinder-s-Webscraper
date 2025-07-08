
from src.utils.file_handler import FileHandler


def test_read_write(tmp_path):
    handler = FileHandler()
    file_path = tmp_path / "sample.txt"
    handler.write(str(file_path), "hello world")

    assert file_path.exists()
    content = handler.read(str(file_path))
    assert content == "hello world"

import os

import pytest

from src.utils.file_handler import FileHandler


@pytest.fixture()
def handler():
    return FileHandler()


def test_write_and_read(tmp_path, handler):
    path = tmp_path / "sample.txt"
    handler.write(str(path), "hello")
    assert path.read_text(encoding="utf-8") == "hello"
    content = handler.read(str(path))
    assert content == "hello"


def test_read_missing(tmp_path, handler):
    missing = tmp_path / "missing.txt"
    with pytest.raises(FileNotFoundError):
        handler.read(str(missing))


def test_write_invalid_path(tmp_path, handler):
    directory = tmp_path / "some_dir"
    directory.mkdir()
    with pytest.raises(OSError):
        handler.write(str(directory), "data")

