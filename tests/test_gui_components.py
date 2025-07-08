from src.gui.main_window import MainWindow
from src.gui.scheduler_dialog import SchedulerDialog
from src.gui.settings_panel import SettingsPanel
from src.gui.website_manager import WebsiteManager


def test_main_window_show():
    window = MainWindow()
    assert window.show() is None


def test_scheduler_dialog_open():
    dlg = SchedulerDialog()
    assert dlg.open() is None


def test_settings_panel_open():
    panel = SettingsPanel()
    assert panel.open() is None


def test_website_manager_add_and_remove():
    manager = WebsiteManager()
    assert manager.add_website("https://example.com") is None
    assert manager.remove_website("https://example.com") is None
