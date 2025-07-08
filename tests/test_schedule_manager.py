import schedule

from src.scheduling.schedule_manager import ScheduleManager
from tests.dummy_module import dummy_task


def dummy():
    pass


def test_add_task(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    job = manager.add_task("task1", dummy, 1)
    assert job in schedule.jobs
    assert manager.list_tasks()["task1"] is job
    manager.close()


def test_remove_task(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    job = manager.add_task("task1", dummy, 1)
    assert manager.remove_task("task1") is True
    assert job not in schedule.jobs
    assert manager.list_tasks() == {}
    manager.close()


def test_list_tasks_multiple(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    job1 = manager.add_task("task1", dummy, 1)
    job2 = manager.add_task("task2", dummy, 2)
    tasks = manager.list_tasks()
    assert set(tasks.keys()) == {"task1", "task2"}
    assert tasks["task1"] is job1
    assert tasks["task2"] is job2
    manager.close()


def test_persistence(tmp_path):
    """Tasks should be reloaded from the SQLite database."""
    db = tmp_path / "sched.db"
    schedule.clear()
    manager = ScheduleManager(db_path=str(db))
    manager.add_task("task1", dummy, 1)
    manager.close()

    schedule.clear()
    manager2 = ScheduleManager(db_path=str(db))
    assert "task1" in manager2.list_tasks()
    job = manager2.list_tasks()["task1"]
    assert job in schedule.jobs
    manager2.close()


def test_tasks_persist_between_instances(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager1 = ScheduleManager(db_path=str(db))
    manager1.add_task("persist", dummy_task, 1)

    schedule.clear()
    manager2 = ScheduleManager(db_path=str(db))
    tasks = manager2.list_tasks()
    assert set(tasks.keys()) == {"persist"}
    assert tasks["persist"].job_func.func == dummy_task


def test_removed_task_not_loaded(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager1 = ScheduleManager(db_path=str(db))
    manager1.add_task("persist", dummy_task, 1)
    manager1.remove_task("persist")

    schedule.clear()
    manager2 = ScheduleManager(db_path=str(db))
    assert manager2.list_tasks() == {}
