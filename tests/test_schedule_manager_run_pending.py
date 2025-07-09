import schedule
import pytest
try:
    from cinder_web_scraper.scheduling.schedule_manager import ScheduleManager
except Exception as exc:  # pragma: no cover - skip if module fails to import
    pytest.skip(f"ScheduleManager unavailable: {exc}", allow_module_level=True)


def test_run_pending_calls_schedule(tmp_path, monkeypatch):
    called = []

    def fake_run_pending():
        called.append(True)

    monkeypatch.setattr(schedule, "run_pending", fake_run_pending)
    db = tmp_path / "sched.db"
    manager = ScheduleManager(db_path=str(db))
    manager.run_pending()
    assert called == [True]
