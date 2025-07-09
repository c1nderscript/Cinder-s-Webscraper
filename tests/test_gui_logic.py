import os
import pytest
from unittest.mock import patch, MagicMock
from cinder_web_scraper.gui.main_window import MainWindow
from cinder_web_scraper.gui.scheduler_dialog import SchedulerDialog
from cinder_web_scraper.gui.settings_panel import SettingsPanel
from cinder_web_scraper.gui.website_manager import WebsiteManager


@pytest.mark.skipif(os.environ.get('CI') == 'true', reason='Skipping GUI tests in CI environment')
@patch('cinder_web_scraper.gui.main_window.tk')
def test_main_window_show_returns_none(mock_tk):
    # Mock tkinter to avoid display issues in CI
    mock_tk.Tk.return_value = MagicMock()
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
