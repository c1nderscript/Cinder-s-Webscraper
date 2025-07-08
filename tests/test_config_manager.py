from src.utils import config_manager


def test_save_and_load(tmp_path):
    data = {"name": "test", "value": 123}
    path = tmp_path / "config.json"
    config_manager.save_config(path, data)
    assert path.exists()
    loaded = config_manager.load_config(path)
    assert loaded == data


def test_load_missing(tmp_path):
    path = tmp_path / "missing.json"
    assert config_manager.load_config(path) == {}
