import builtins
from src.utils.file_handler import FileHandler
from src.utils.logger import Logger


def test_file_handler_methods_return_none(tmp_path):
    fh = FileHandler()
    assert fh.read(str(tmp_path / 'file.txt')) is None
    assert fh.write(str(tmp_path / 'file.txt'), 'data') is None


def test_logger_log_returns_none():
    logger = Logger()
    assert logger.log('message') is None
