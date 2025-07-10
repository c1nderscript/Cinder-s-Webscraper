from unittest.mock import MagicMock, patch

from cinder_web_scraper.utils.repo_updater import update_repo


@patch("cinder_web_scraper.utils.repo_updater.subprocess.run")
def test_update_repo_success(mock_run):
    mock_run.return_value = MagicMock(returncode=0, stderr="", stdout="")
    assert update_repo() is True
    mock_run.assert_called_with(["git", "pull"], capture_output=True, text=True, check=False)


@patch("cinder_web_scraper.utils.repo_updater.subprocess.run")
def test_update_repo_failure(mock_run):
    mock_run.return_value = MagicMock(returncode=1, stderr="error", stdout="")
    assert update_repo() is False


@patch("cinder_web_scraper.utils.repo_updater.subprocess.run", side_effect=OSError)
def test_update_repo_exception(mock_run):
    assert update_repo() is False
