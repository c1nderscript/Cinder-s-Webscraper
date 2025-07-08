from src.gui.main_window import MainWindow
from src.gui.website_manager import WebsiteManager
from src.gui.scheduler_dialog import SchedulerDialog
from src.gui.settings_panel import SettingsPanel


def test_main_window_show():
    window = MainWindow()
    result = window.show()
    assert result is None


def test_website_manager_methods():
    manager = WebsiteManager()
    add_result = manager.add_website("http://example.com")
    remove_result = manager.remove_website("http://example.com")
    assert add_result is None
    assert remove_result is None


def test_scheduler_dialog_open():
    dialog = SchedulerDialog()
    result = dialog.open()
    assert result is None


def test_settings_panel_open():
    panel = SettingsPanel()
    result = panel.open()
    assert result is None
