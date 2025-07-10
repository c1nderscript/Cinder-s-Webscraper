# Cinder's Web Scraper

[![CI](https://github.com/OWNER/Cinder-s-Webscraper/actions/workflows/python.yml/badge.svg)](https://github.com/OWNER/Cinder-s-Webscraper/actions/workflows/python.yml)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)

## Project Overview


Cinder's Web Scraper is a Windows-focused GUI application that helps you configure and schedule web scraping tasks without writing code. Configuration is stored in easy-to-edit JSON files and the application manages recurring jobs using the [`schedule`](https://pypi.org/project/schedule/) library.

A GUI-based web scraper application for Windows systems built with Python. The application enables users to configure, schedule, and manage web scraping tasks through an intuitive interface. Configuration files are stored in JSON format and saved under the `data/` directory.


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


- Requires **Python 3.8+**
- Install the package and its dependencies:

```bash
pip install .
```

For development, include optional dependencies:

```bash
pip install .[dev]

Follow these steps to get a local development environment running on
Windows 10/11. The instructions also work on other platforms with a
compatible Python interpreter.

1. Install **Python 3.8** or later and make sure ``python`` is available in
   your ``PATH``.
2. Clone this repository:

   ```bash
   git clone https://github.com/your-user/cinder-webscraper.git
   cd cinder-webscraper
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
python main.py
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
2. Run `python main.py` (or use the GUI) to start the scheduler.
3. Scraped data appears in the `output/` directory following the configured format.

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

## Contributing

Contributions are welcome! Please run `pytest` before submitting a pull request.

and a job named ``dummy`` will run every five seconds until you press
``Ctrl+C``.

### Graphical interface

A basic Tkinter interface is included but is still under development. You
can experiment with the placeholder window using the following snippet:

```bash
python - <<'PY'
from cinder_web_scraper.gui.main_window import MainWindow

window = MainWindow()
window.show()
PY
```

Future releases will bundle a launcher script that opens the GUI directly.

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

## Example Scraping Workflow

1. Edit `data/websites.json` to define the URLs and CSS selectors to scrape.
2. Launch the GUI to schedule scraping tasks at custom intervals.
3. The `ScheduleManager` (recently documented and tested) handles task timing.
4. Results are saved under `output/scraped_data/` using the `OutputManager` placeholder.

This workflow highlights the new configuration tests and schedule manager features added in the previous tasks.

## Contributing

Please see the [Developer Guide](docs/DEVELOPER_GUIDE.md) for detailed
contribution instructions. In short:

1. Fork the repository and create a feature branch.
2. Install dependencies and run ``pytest`` before submitting a pull request.
3. Keep commits focused and provide clear descriptions of your changes.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

