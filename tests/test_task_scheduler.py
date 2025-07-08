from cinder_web_scraper.scheduling.task_scheduler import TaskScheduler


def test_add_and_run():
    scheduler = TaskScheduler()
    results = []

    def sample(x):
        results.append(x)

    scheduler.add_task(sample, 5)
    scheduler.add_task(sample, 10)
    scheduler.run_all()

    assert results == [5, 10]
    assert scheduler.tasks == []
