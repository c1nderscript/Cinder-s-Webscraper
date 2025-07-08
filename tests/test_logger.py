from src.utils.logger import Logger


def test_log_output(tmp_path):
    log_file = tmp_path / "test.log"
    logger = Logger("test", log_file=str(log_file))
    logger.log("sample message")

    assert log_file.exists()
    contents = log_file.read_text()
    assert "sample message" in contents
