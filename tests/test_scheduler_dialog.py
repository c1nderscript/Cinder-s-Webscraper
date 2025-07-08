from unittest.mock import MagicMock, patch

from src.gui.scheduler_dialog import SchedulerDialog


class DummyVar:
    def __init__(self, value):
        self._value = value

    def get(self):
        return self._value


def test_schedule_valid():
    manager = MagicMock()
    dialog = SchedulerDialog(None, manager)
    dialog.name_var = DummyVar('task1')
    dialog.interval_var = DummyVar(10)
    dialog.window = MagicMock()
    with (
        patch('src.gui.scheduler_dialog.messagebox.showinfo') as mock_info,
        patch('src.gui.scheduler_dialog.messagebox.showerror') as mock_error,
    ):
        dialog._on_add()
        manager.add_task.assert_called_once()
        mock_info.assert_called_once()
        mock_error.assert_not_called()
        dialog.window.destroy.assert_called_once()


def test_schedule_invalid():
    manager = MagicMock()
    dialog = SchedulerDialog(None, manager)
    dialog.name_var = DummyVar('')
    dialog.interval_var = DummyVar(-1)
    dialog.window = MagicMock()
    with patch('src.gui.scheduler_dialog.messagebox.showerror') as mock_error:
        dialog._on_add()
        manager.add_task.assert_not_called()
        mock_error.assert_called_once()
        dialog.window.destroy.assert_not_called()
