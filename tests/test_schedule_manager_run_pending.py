import schedule
from cinder_web_scraper.scheduling import ScheduleManager


def test_run_pending_calls_schedule(monkeypatch):
    called = []

    def fake_run_pending():
        called.append(True)

    monkeypatch.setattr(schedule, "run_pending", fake_run_pending)
    manager = ScheduleManager()
    manager.run_pending()
    assert called == [True]
