from unittest.mock import patch
import subprocess

from cinder_web_scraper.utils import updater
from cinder_web_scraper.utils.updater import update_application


@patch('cinder_web_scraper.utils.updater.subprocess.run')
def test_update_repo_calls_git_pull(mock_run):
    mock_run.return_value = None
    assert updater.update_repo() is True
    mock_run.assert_called_once_with(
        ['git', 'pull', 'origin'],
        check=True,
        capture_output=True,
        text=True,
    )


def test_update_application_success():
    cp = subprocess.CompletedProcess(['git', 'pull'], 0, stdout='ok', stderr='')
    with patch('subprocess.run', return_value=cp) as run:
        success, msg = update_application()
        run.assert_called_once()
        assert success is True
        assert 'ok' in msg


def test_update_application_failure():
    err = subprocess.CalledProcessError(1, ['git', 'pull'], stderr='fail')
    with patch('subprocess.run', side_effect=err) as run:
        success, msg = update_application()
        run.assert_called_once()
        assert success is False
        assert 'fail' in msg
