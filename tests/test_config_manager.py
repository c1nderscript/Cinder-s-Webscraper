from src.utils import config_manager


def test_save_and_load(tmp_path):
    data = {"name": "test", "value": 123}
    path = tmp_path / "config.json"
    success = config_manager.save_config(data, str(path))
    assert success is True
    assert path.exists()
    loaded = config_manager.load_config(str(path))
    assert loaded == data


def test_load_missing(tmp_path):
    path = tmp_path / "missing.json"
    loaded = config_manager.load_config(str(path))
    assert loaded == {"websites": [], "settings": {}}


def test_load_malformed(tmp_path):
    """Load a file containing malformed JSON and ensure defaults are returned."""
    path = tmp_path / "malformed.json"
    path.write_text("{ invalid json [")
    loaded = config_manager.load_config(str(path))
    assert loaded == config_manager.DEFAULT_CONFIG


def test_default_path(tmp_path, monkeypatch):
    data = {"foo": "bar"}
    default_path = tmp_path / "default.json"
    monkeypatch.setattr(config_manager, "DEFAULT_CONFIG_PATH", str(default_path))
    monkeypatch.setattr(config_manager.load_config, "__defaults__", (str(default_path),))
    monkeypatch.setattr(config_manager.save_config, "__defaults__", (str(default_path),))

    # Should save to the patched default path
    assert config_manager.save_config(data) is True
    assert default_path.exists()

    loaded = config_manager.load_config()
    assert loaded == data
