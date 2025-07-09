
from cinder_web_scraper.utils.logger import Logger


def test_log_output(tmp_path):
    log_file = tmp_path / "test.log"
    logger = Logger("test", log_file=str(log_file))
    logger.log("sample message")

    assert log_file.exists()
    contents = log_file.read_text()
    assert "sample message" in contents

import logging

from cinder_web_scraper.utils.logger import get_logger, log_exception


def test_get_logger_returns_logger():
    logger = get_logger("test")
    assert isinstance(logger, logging.Logger)


def test_log_exception_does_not_raise():
    logger = get_logger("test_exception")
    try:
        raise ValueError("boom")
    except ValueError as exc:
        log_exception(logger, "testing", exc)


