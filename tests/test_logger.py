from src.utils.logger import Logger


def test_log_file_creation(tmp_path):
    log_path = tmp_path / "scraper.log"
    logger = Logger(__name__, log_file=str(log_path))
    logger.info("info message")
    logger.warning("warn message")
    logger.error("error message")

    assert log_path.exists()
    content = log_path.read_text()
    assert "info message" in content
    assert "warn message" in content
    assert "error message" in content
