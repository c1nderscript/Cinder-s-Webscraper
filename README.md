# Cinder's Web Scraper

[![CI](https://github.com/c1nderscript/Cinder-s-Webscraper/actions/workflows/python.yml/badge.svg)](https://github.com/c1nderscript/Cinder-s-Webscraper/actions/workflows/python.yml)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)

## Project Overview


Cinder's Web Scraper is a Windows-focused GUI application that helps you configure and schedule web scraping tasks without writing code. Configuration is stored in easy-to-edit JSON files and the application manages recurring jobs using the [`schedule`](https://pypi.org/project/schedule/) library.


## Features

- **Website Management** – add or remove URLs and keep per-site settings
- **Scraping Rules** – define selectors and extraction rules for each website
- **Scheduling** – run scrapes at fixed intervals using a simple scheduler
- **File Management** – save scraped data to custom output folders
- **Logging** – record scraper activity and errors to `data/logs/scraper.log`

This repository currently contains a minimal scheduling example, but the directory structure prepares for a full desktop application.

## Installation


1. Install **Python 3.8+**
2. Install the project dependencies:



```bash
pip install .
```

For development, include optional dependencies:

```bash
pip install .[dev]
```

Follow these steps to get a local development environment running on
Windows 10/11. The instructions also work on other platforms with a
compatible Python interpreter.

1. Install **Python 3.8** or later and make sure ``python`` is available in
   your ``PATH``.
2. Clone this repository:

   ```bash
   git clone https://github.com/c1nderscript/Cinder-s-Webscraper.git
   cd Cinder-s-Webscraper
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/macOS
   source venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the test suite to verify your setup:

   ```bash
   pytest
   ```

## Data Directory

Configuration, schedules and log files are stored in the `data/` folder:

- `data/websites.json` – website configuration managed by `config_manager`
- `data/schedules.db` – SQLite database created by the scheduler
- `data/logs/` – directory for application log files

- Create the required data directories and files:


```bash
mkdir -p data/logs
touch data/websites.json data/schedules.db

```

## Directory Layout

```
project_root/
├── cinder_web_scraper/  # Application code
│   ├── gui/
│   ├── scraping/
│   ├── scheduling/
│   └── utils/
├── data/      # Configuration files and logs
│   ├── websites.json
│   ├── schedules.db
│   └── logs/
├── output/    # Scraped data is written here
└── tests/
```

`data/` holds user configuration and log files while all scraped results are written to `output/`.


## Configuration Helpers

- `load_config(path=None)` – Load a configuration from a file. If ``path`` is omitted or the file does not exist, a default configuration is returned.
- `save_config(data, path=None)` – Save a configuration dictionary to ``path``. When ``path`` is omitted the data is written to `data/websites.json`.


The `config_manager` module in `cinder_web_scraper.utils` provides convenience functions:

```python
from cinder_web_scraper.utils.config_manager import load_config, save_config


config = load_config("data/config.json")
config["settings"]["debug"] = True
save_config(config, "data/config.json")

# Load configuration or get defaults
config = load_config()

# Modify configuration as needed
config["settings"]["debug"] = True

# Save the updated configuration
save_success = save_config(config)

```

Configuration files can be edited manually or through the planned GUI interface.


## Running the Application

### Command-line demo

Run the scheduler demo with:

### Command-line

The repository currently ships with a small command-line demo. Execute


```bash
python -m cinder_web_scraper
```


You will see a simple loop that executes a dummy job every few seconds.

### GUI application

The GUI components live in `cinder_web_scraper/gui`. During development you can launch the (placeholder) main window with:

```bash
python -m cinder_web_scraper.gui.main_window
```

As features are implemented, this will provide buttons to manage websites, scheduling options, and view logs.


## Example Workflow

1. Edit `data/websites.json` to add the sites you want to scrape.
2. Run `python -m cinder_web_scraper` (or use the GUI) to start the scheduler.
3. Scraped data appears in the `output/` directory following the configured format.
4. Click **Update** in the GUI toolbar to pull the latest code from your configured remote.

## Logging Configuration

Logging is configured to write to `data/logs/scraper.log` and to the console:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("data/logs/scraper.log"),
        logging.StreamHandler(),
    ],
)
```


## Updating the Repository

The GUI offers a convenient way to pull the latest changes. Choose
**Tools → Update Repo** from the menu and confirm the prompt. The application
will run ``git pull`` and notify you whether the update succeeded.

## Troubleshooting

If the application fails to start or tests do not run, try the following:

1. **Verify Python version** – run ``python --version`` and ensure it is
   3.8 or newer.
2. **Dependencies** – reinstall packages with ``pip install -r requirements.txt``.
3. **Virtual environment issues** – deactivate and recreate the virtual
   environment if modules are missing.
4. **Update button errors** – confirm the repository has a configured remote
   and that your Git credentials allow pulling updates. Commit or stash local
   changes if merge conflicts occur.

## FAQ

**Q: Does the scraper work on macOS or Linux?**

Yes. Although the project targets Windows, the code is pure Python and can run
on other platforms with only minor adjustments.

**Q: Where is scraped data stored?**

By default, files are saved under the ``output/`` directory. You can change the
path in your configuration file.

## Launching the GUI

A basic Tkinter interface is provided in `cinder_web_scraper/gui`. To start the GUI, run:

```bash
python -m cinder_web_scraper.gui.main_window
```

The GUI currently contains placeholder widgets but demonstrates how to integrate the scheduling system. The recent tasks added docstrings and type hints across these modules, making it easier to understand and extend the GUI code.

## Configuration Files

Configuration data is stored under the `data/` directory:

- `data/config.json` – General settings and website list
- `data/websites.json` – Individual website profiles
- `data/schedules.db` – Planned job database

These files are created automatically when saving via `config_manager` or scheduling utilities. Logs are written to `data/logs/`.

## Update Button

The GUI provides an **Update** button that pulls the latest changes from your configured Git remote. Clicking the button is equivalent to running:

```bash
git pull --ff-only
```

### Prerequisites

1. The scraper directory must be a Git repository with a remote (typically `origin`).
2. If your remote requires authentication, ensure your credentials are saved via SSH keys or a credential helper so `git pull` can succeed.

### How it Works

When the button is pressed the application executes `git pull` in the project folder. If there are uncommitted local changes that would result in a merge conflict, the update is cancelled and an error message is displayed.


## Example Scraping Workflow

1. Edit `data/websites.json` to define the URLs and CSS selectors to scrape.
2. Launch the GUI to schedule scraping tasks at custom intervals.
3. The `ScheduleManager` handles task timing and can be used as a context
   manager for automatic cleanup:

   ```python
   from cinder_web_scraper.scheduling import ScheduleManager

   with ScheduleManager() as manager:
       manager.add_task("demo", lambda: print("run"), 5)
       manager.run_pending()
   ```

4. Results are saved under `output/` using the `OutputManager` placeholder.

This workflow highlights the new configuration tests and schedule manager features added in the previous tasks.

## Contributing

Please see the [Developer Guide](docs/DEVELOPER_GUIDE.md) for detailed
contribution instructions. In short:

1. Fork the repository and create a feature branch.
2. Install dependencies and run ``pytest`` before submitting a pull request.
3. Keep commits focused and provide clear descriptions of your changes.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

