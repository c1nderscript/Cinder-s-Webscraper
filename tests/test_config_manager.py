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
    path = tmp_path / "malformed.json"
    path.write_text("{ invalid json [")
    loaded = config_manager.load_config(str(path))
    assert loaded == config_manager.DEFAULT_CONFIG


def test_load_config_oserror(monkeypatch):
    def raise_os_error(*args, **kwargs):
        raise OSError

    monkeypatch.setattr('builtins.open', raise_os_error)
    result = config_manager.load_config('dummy.json')
    assert result == config_manager.DEFAULT_CONFIG


def test_save_config_failure(monkeypatch, tmp_path):
    def raise_os_error(*args, **kwargs):
        raise OSError

    monkeypatch.setattr('builtins.open', raise_os_error)
    success = config_manager.save_config({}, str(tmp_path / 'out.json'))
    assert success is False
