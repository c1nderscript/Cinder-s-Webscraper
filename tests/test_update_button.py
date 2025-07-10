from unittest.mock import MagicMock, patch

from cinder_web_scraper.gui.main_window import MainWindow


@patch('cinder_web_scraper.gui.main_window.update_application')
@patch('cinder_web_scraper.gui.main_window.messagebox')
@patch('cinder_web_scraper.gui.main_window.tk')
def test_update_button_success(mock_tk, mock_msg, mock_update):
    mock_tk.Tk.return_value = MagicMock()
    mock_update.return_value = (True, 'done')
    window = MainWindow(mock_tk.Tk())
    window._update_app()
    mock_update.assert_called_once()
    mock_msg.showinfo.assert_called_once()


@patch('cinder_web_scraper.gui.main_window.update_application')
@patch('cinder_web_scraper.gui.main_window.messagebox')
@patch('cinder_web_scraper.gui.main_window.tk')
def test_update_button_failure(mock_tk, mock_msg, mock_update):
    mock_tk.Tk.return_value = MagicMock()
    mock_update.return_value = (False, 'err')
    window = MainWindow(mock_tk.Tk())
    window._update_app()
    mock_update.assert_called_once()
    mock_msg.showerror.assert_called_once()
