from unittest.mock import patch

from cinder_web_scraper.utils import updater


@patch('cinder_web_scraper.utils.updater.subprocess.run')
def test_update_repo_calls_git_pull(mock_run):
    mock_run.return_value = None
    assert updater.update_repo() is True
    mock_run.assert_called_once_with(
        ['git', 'pull'], check=True, capture_output=True, text=True
    )
