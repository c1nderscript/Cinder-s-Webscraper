import logging

from src.utils.logger import get_logger, log_exception


def test_get_logger_returns_logger():
    logger = get_logger("test")
    assert isinstance(logger, logging.Logger)


def test_log_exception_does_not_raise():
    logger = get_logger("test_exception")
    try:
        raise ValueError("boom")
    except ValueError as exc:
        log_exception(logger, "testing", exc)

