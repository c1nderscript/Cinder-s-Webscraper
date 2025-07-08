import schedule
from src.scheduling.schedule_manager import ScheduleManager


def dummy():
    pass


def test_add_task():
    schedule.clear()
    manager = ScheduleManager()
    job = manager.add_task("task1", dummy, 1)
    assert job in schedule.jobs
    assert manager.list_tasks()["task1"] is job


def test_remove_task():
    schedule.clear()
    manager = ScheduleManager()
    job = manager.add_task("task1", dummy, 1)
    assert manager.remove_task("task1") is True
    assert job not in schedule.jobs
    assert manager.list_tasks() == {}


def test_list_tasks_multiple():
    schedule.clear()
    manager = ScheduleManager()
    job1 = manager.add_task("task1", dummy, 1)
    job2 = manager.add_task("task2", dummy, 2)
    tasks = manager.list_tasks()
    assert set(tasks.keys()) == {"task1", "task2"}
    assert tasks["task1"] is job1
    assert tasks["task2"] is job2
