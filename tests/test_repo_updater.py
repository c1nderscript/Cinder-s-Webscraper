from unittest.mock import MagicMock, patch
import subprocess

from cinder_web_scraper.utils.updater import update_repo


@patch("cinder_web_scraper.utils.updater.subprocess.run")
def test_update_repo_success(mock_run):
    mock_run.return_value = MagicMock(returncode=0, stderr="", stdout="")
    assert update_repo() is True
    mock_run.assert_called_with(
        ["git", "pull", "origin"], check=True, capture_output=True, text=True
    )


@patch("cinder_web_scraper.utils.updater.subprocess.run")
def test_update_repo_failure(mock_run):
    mock_run.side_effect = subprocess.CalledProcessError(1, ["git", "pull"])
    assert update_repo() is False


@patch("cinder_web_scraper.utils.updater.subprocess.run", side_effect=OSError)
def test_update_repo_exception(mock_run):
    assert update_repo() is False
