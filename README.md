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

## Contributing

Contributions are welcome! Guidelines will be provided soon.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
