import os
import pytest
from unittest.mock import patch, MagicMock

from src.gui.scheduler_dialog import SchedulerDialog
from src.gui.settings_panel import SettingsPanel
from src.gui.website_manager import WebsiteManager


@pytest.mark.skipif(os.environ.get('CI') == 'true', reason='Skipping GUI tests in CI environment')
def test_main_window_show_returns_none():
    # Mock tkinter to avoid display issues in CI
    with patch('tkinter.Tk') as mock_tk:
        mock_root = MagicMock()
        mock_tk.return_value = mock_root
        
        from src.gui.main_window import MainWindow
        window = MainWindow()
        assert window.show() is None


def test_scheduler_dialog_open_returns_none():
    dialog = SchedulerDialog()
    assert dialog.open() is None


def test_settings_panel_open_returns_none():
    panel = SettingsPanel()
    assert panel.open() is None


def test_website_manager_methods_return_none():
    manager = WebsiteManager()
    assert manager.add_website('http://example.com') is None
    assert manager.remove_website('http://example.com') is None
