import schedule
from src.scheduling.schedule_manager import ScheduleManager


def dummy():
    pass


def test_add_task(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    job = manager.add_task("task1", dummy, 1)
    assert job in schedule.jobs
    assert manager.list_tasks()["task1"] is job
    assert manager.get_schedule("task1") == {"name": "task1", "interval": 1}


def test_remove_task(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    job = manager.add_task("task1", dummy, 1)
    assert manager.remove_task("task1") is True
    assert job not in schedule.jobs
    assert manager.list_tasks() == {}
    assert manager.get_schedule("task1") is None


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


def test_crud_operations(tmp_path):
    schedule.clear()
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))

    # create
    manager.create_schedule("task1", 5)
    assert manager.get_schedule("task1") == {"name": "task1", "interval": 5}

    # update
    assert manager.update_schedule("task1", 10) is True
    assert manager.get_schedule("task1") == {"name": "task1", "interval": 10}

    # list
    manager.create_schedule("task2", 3)
    schedules = manager.list_schedules()
    assert {s["name"] for s in schedules} == {"task1", "task2"}

    # delete
    assert manager.delete_schedule("task1") is True
    assert manager.get_schedule("task1") is None
