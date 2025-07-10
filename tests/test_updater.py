import subprocess
from unittest.mock import patch

import pytest

from cinder_web_scraper.utils.updater import update_application


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
