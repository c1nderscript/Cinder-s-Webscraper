# Cinder's Web Scraper

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](#)
[![License](https://img.shields.io/badge/license-MIT-blue)](#license)

## Project Overview

A GUI-based web scraper application for Windows systems built with Python. The application enables users to configure, schedule, and manage web scraping tasks through an intuitive interface. Configuration files are stored in JSON format.

This repository contains a minimal scheduling example using the [`schedule`](https://pypi.org/project/schedule/) package.

## Installation

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

### Command-line

The repository currently ships with a small command-line demo. Execute

```bash
python main.py
```

and a job named ``dummy`` will run every five seconds until you press
``Ctrl+C``.

### Graphical interface

A basic Tkinter interface is included but is still under development. You
can experiment with the placeholder window using the following snippet:

```bash
python - <<'PY'
from src.gui.main_window import MainWindow

window = MainWindow()
window.show()
PY
```

Future releases will bundle a launcher script that opens the GUI directly.

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

## Contributing

Please see the [Developer Guide](docs/DEVELOPER_GUIDE.md) for detailed
contribution instructions. In short:

1. Fork the repository and create a feature branch.
2. Install dependencies and run ``pytest`` before submitting a pull request.
3. Keep commits focused and provide clear descriptions of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
