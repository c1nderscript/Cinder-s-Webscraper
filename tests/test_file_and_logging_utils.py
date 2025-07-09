import builtins
import pytest
from cinder_web_scraper.utils.file_handler import FileHandler
from cinder_web_scraper.utils.logger import get_logger


def test_file_handler_methods_return_none(tmp_path):
    fh = FileHandler()
    with pytest.raises(FileNotFoundError):
        fh.read(str(tmp_path / 'file.txt'))
    assert fh.write(str(tmp_path / 'file.txt'), 'data') is None


def test_logger_get_logger_returns_logger():
    logger = get_logger('test')
    assert logger is not None
    assert logger.name == 'test'
