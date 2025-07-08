# Cinder's Web Scraper

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)

## Project Overview

A GUI-based web scraper application for Windows systems built with Python. The application enables users to configure, schedule, and manage web scraping tasks through an intuitive interface. Configuration files are stored in JSON format.

This repository contains a minimal scheduling example using the [`schedule`](https://pypi.org/project/schedule/) package.

## Installation

- Requires **Python 3.8+**
- Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration Helpers

The `config_manager` module offers two helper functions:

- `load_config(path)` – Load a configuration from a file. If the file does not exist or contains invalid JSON, a default configuration is returned.
- `save_config(data, path)` – Save a configuration dictionary to the specified path.

Example usage:

```python
from src.utils.config_manager import load_config, save_config

# Load configuration or get defaults
config = load_config("data/config.json")

# Modify configuration as needed
config["settings"]["debug"] = True

# Save the updated configuration
save_success = save_config(config, "data/config.json")
```

## Usage

Run the application with:

```bash
python main.py
```

This will start a simple scheduler that prints a message every few seconds.

## Launching the GUI

A basic Tkinter interface is provided in `src/gui`. To start the GUI, run:

```bash
python -m src.gui.main_window
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

Contributions are welcome! Guidelines will be provided soon.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
