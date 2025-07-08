from pathlib import Path
import logging

from src.utils import logger as logger_module


def test_configure_creates_log_file(tmp_path):
    log_file = tmp_path / "scraper.log"

    # reset logging configuration for the test
    logger_module._CONFIGURED = False
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logger_module.configure(log_file)
    log = logger_module.get_logger("test")
    log.info("test message")

    assert log_file.exists()
    content = log_file.read_text()
    assert "test message" in content
