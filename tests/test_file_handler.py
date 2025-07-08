from src.utils.file_handler import FileHandler


def test_read_write(tmp_path):
    handler = FileHandler()
    file_path = tmp_path / "sample.txt"
    handler.write(str(file_path), "hello world")

    assert file_path.exists()
    content = handler.read(str(file_path))
    assert content == "hello world"
