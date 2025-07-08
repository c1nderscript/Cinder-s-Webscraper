import pytest
from unittest.mock import patch

from src.gui.website_manager import WebsiteManager


def test_add_valid_url():
    manager = WebsiteManager(None)
    with patch('src.gui.website_manager.messagebox.showinfo') as mock_info, \
         patch('src.gui.website_manager.messagebox.showerror') as mock_error:
        manager.add_website('http://example.com')
        assert 'http://example.com' in manager.websites
        mock_info.assert_called_once()
        mock_error.assert_not_called()


def test_add_invalid_url():
    manager = WebsiteManager(None)
    with patch('src.gui.website_manager.messagebox.showerror') as mock_error:
        manager.add_website('invalid-url')
        assert manager.websites == []
        mock_error.assert_called_once()


def test_remove_website_not_found():
    manager = WebsiteManager(None)
    with patch('src.gui.website_manager.messagebox.showerror') as mock_error:
        manager.remove_website('http://missing.com')
        mock_error.assert_called_once()


def test_remove_existing_url():
    manager = WebsiteManager(None)
    manager.websites = ['http://example.com']
    with patch('src.gui.website_manager.messagebox.showinfo') as mock_info, \
         patch('src.gui.website_manager.messagebox.showerror') as mock_error:
        manager.remove_website('http://example.com')
        assert manager.websites == []
        mock_info.assert_called_once()
        mock_error.assert_not_called()
