import pytest
from cinder_web_scraper.utils.file_handler import FileHandler
from cinder_web_scraper.utils.logger import get_logger



def test_file_handler_read_write(tmp_path):
    fh = FileHandler()
    file_path = tmp_path / 'file.txt'
    fh.write(str(file_path), 'data')
    assert file_path.exists()
    assert fh.read(str(file_path)) == 'data'

def test_file_handler_methods(tmp_path):
    fh = FileHandler()
    missing = tmp_path / 'file.txt'
    with pytest.raises(FileNotFoundError):
        fh.read(str(missing))
    fh.write(str(missing), 'data')
    assert fh.read(str(missing)) == 'data'



def test_logger_get_logger_returns_logger():
    logger = get_logger('test')
    assert logger is not None
    assert logger.name == 'test'
