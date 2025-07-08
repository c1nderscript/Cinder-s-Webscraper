from unittest.mock import MagicMock, patch

from src.gui.settings_panel import SettingsPanel


class DummyVar:
    def __init__(self, value):
        self._value = value

    def get(self):
        return self._value


def test_save_settings():
    config = {"debug": False}
    panel = SettingsPanel(None, config)
    panel.debug_var = DummyVar(True)
    panel.window = MagicMock()
    with patch('src.gui.settings_panel.messagebox.showinfo') as mock_info:
        panel._save()
        assert config["debug"] is True
        mock_info.assert_called_once()
        panel.window.destroy.assert_called_once()
