# Cinder's Web Scraper

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
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
pip install -r requirements.txt
```

## Directory Layout

```
project_root/
├── data/      # Configuration files and logs
│   ├── websites.json
│   ├── schedules.db
│   └── logs/
├── output/    # Scraped data is written here
└── src/       # Application code
```

`data/` holds user configuration and log files while all scraped results are written to `output/`.

## Configuration Helpers

The `config_manager` module in `src/utils` provides convenience functions:

```python
from src.utils.config_manager import load_config, save_config

config = load_config("data/config.json")
config["settings"]["debug"] = True
save_config(config, "data/config.json")
```

Configuration files can be edited manually or through the planned GUI interface.

## Running the Application

### Command-line demo

Run the scheduler demo with:

```bash
python main.py
```

You will see a simple loop that executes a dummy job every few seconds.

### GUI application

The GUI components live in `src/gui`. During development you can launch the (placeholder) main window with:

```bash
python -m src.gui.main_window
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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
