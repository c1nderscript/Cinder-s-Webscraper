from unittest.mock import MagicMock, patch
from cinder_web_scraper.gui.main_window import MainWindow
from cinder_web_scraper.gui.scheduler_dialog import SchedulerDialog
from cinder_web_scraper.gui.settings_panel import SettingsPanel
from cinder_web_scraper.gui.website_manager import WebsiteManager


@patch('cinder_web_scraper.gui.main_window.tk')
def test_main_window_show(mock_tk):
    root = mock_tk.Tk()
    window = MainWindow(root)
    assert window.show() is None


@patch('cinder_web_scraper.gui.scheduler_dialog.tk')
def test_scheduler_dialog_open(mock_tk):
    parent = mock_tk.Tk()
    dlg = SchedulerDialog(parent=parent)
    assert dlg.open() is None


@patch('cinder_web_scraper.gui.settings_panel.tk')
def test_settings_panel_open(mock_tk):
    parent = mock_tk.Tk()
    panel = SettingsPanel(parent=parent)
    assert panel.open() is None


def test_website_manager_add_and_remove():
    manager = WebsiteManager()
    assert manager.add_website("https://example.com") is None
    assert manager.remove_website("https://example.com") is None
