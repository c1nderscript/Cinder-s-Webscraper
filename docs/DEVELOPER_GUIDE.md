# Developer Guide

This document provides an overview of the code base, contribution process and a reference for the public APIs.

## Code Structure

```
cinder_web_scraper/
├── gui/                # Tkinter GUI components
├── scraping/           # Future scraping engine
├── scheduling/         # Task scheduling modules
├── utils/              # Utility helpers
```

- **cinder_web_scraper/gui** – Placeholder classes for the Tkinter interface such as `MainWindow`, `WebsiteManager`, `SchedulerDialog` and `SettingsPanel`.
- **cinder_web_scraper/scheduling** – Implements simple scheduling logic. `ScheduleManager` wraps the [`schedule`](https://pypi.org/project/schedule/) library and `TaskScheduler` provides an in-memory queue.
- **cinder_web_scraper/utils** – Helper modules such as `config_manager` for reading/writing JSON config files.

## Contributing

1. Fork the repository on GitHub and create a feature branch.
2. Install the project dependencies with `pip install -r requirements.txt`.
3. Run `pytest` to ensure all tests pass before submitting changes.
4. Create a pull request describing your changes.

We follow standard Python style with informative docstrings. Please keep commit messages clear and concise.

## API Reference

### `cinder_web_scraper.utils.config_manager`

- `load_config(path)` – Return a configuration dictionary from `path`. If the file does not exist or is malformed, default settings are returned.
- `save_config(data, path)` – Save a configuration dictionary to the given path. Returns `True` on success.

### `cinder_web_scraper.scheduling.schedule_manager`

- `add_task(name, func, interval)` – Schedule `func` to run every `interval` seconds. Returns the created job object.
- `remove_task(name)` – Cancel a scheduled job by name. Returns `True` if removed.
- `list_tasks()` – Return a mapping of task names to jobs.
- `run_pending()` – Execute any tasks that are due to run.

### `cinder_web_scraper.scheduling.task_scheduler`

- `add_task(func, *args, **kwargs)` – Queue a callable with optional arguments.
- `run_all()` – Execute queued callables in order and clear the queue.

GUI classes currently contain placeholders and will be expanded in future releases.
