# Cinder's Web Scraper - agents.md

## Project Overview

A GUI-based web scraper application for Windows systems built with Python. The application enables users to configure, schedule, and manage web scraping tasks through an intuitive Tkinter interface. This project focuses on user-friendly web scraping with robust scheduling capabilities and flexible data output options.

**Current Development Phase**: Early development with basic scheduling functionality implemented  
**Primary Goal**: Create a comprehensive desktop application for non-technical users to perform web scraping tasks  
**Target Platform**: Windows 10/11 with Python 3.8+ support  

## Core Features

### 1. Website Management
- **Add/Remove Websites**: Users can add URLs they want to scrape
- **Website Profiles**: Save scraping configurations for different sites
- **URL Validation**: Ensure valid URLs before adding to scrape list
- **Site Categories**: Organize websites by category or purpose

### 2. Scraping Configuration
- **Content Selectors**: CSS selectors or XPath for specific elements
- **Data Extraction Rules**: Define what data to extract (text, images, links, etc.)
- **Output Formats**: Support for CSV, JSON, XML, and plain text
- **Custom Headers**: User-agent strings and custom HTTP headers
- **Request Delays**: Configurable delays between requests

### 3. Scheduling System
- **Timer-based Scraping**: Regular intervals (minutes, hours, days)
- **Cron-like Scheduling**: Specific times and dates
- **One-time Scraping**: Immediate execution option
- **Schedule Management**: View, edit, and delete scheduled tasks

### 4. File Management
- **Custom Save Paths**: User-specified output directories
- **File Naming Conventions**: Timestamp-based or custom naming
- **File Organization**: Automatic folder structure creation
- **Backup System**: Keep previous scraping results

### 5. GUI Components
- **Main Dashboard**: Overview of all scraping tasks
- **Website Manager**: Add/edit/remove websites
- **Scheduler Interface**: Configure timing and frequency
- **Settings Panel**: Application configuration
- **Log Viewer**: Real-time scraping status and errors
- **Progress Indicators**: Visual feedback during scraping

## Technical Architecture

### Core Components

#### 1. GUI Framework
- **Primary**: Tkinter (built-in Python GUI library)
- **Alternative**: PyQt5/PyQt6 for advanced features
- **Styling**: Modern, Windows-native appearance

#### 2. Web Scraping Engine
- **HTTP Requests**: `requests` library for web communication
- **HTML Parsing**: `BeautifulSoup4` for content extraction
- **JavaScript Support**: `selenium` for dynamic content (optional)
- **Rate Limiting**: Built-in request throttling

#### 3. Data Storage
- **Configuration**: JSON files for settings and website profiles
- **Scheduling**: SQLite database for task management
- **Scraped Data**: User-specified formats and locations

#### 4. Scheduling System
- **Task Scheduler**: `schedule` library for Python
- **Background Processing**: Threading for non-blocking operations
- **Persistence**: Save and restore scheduled tasks

## Project Structure

```
cinder-webscraper/
├── src/
│   ├── gui/                    # Tkinter GUI components
│   │   ├── main_window.py      # Main application window
│   │   ├── website_manager.py  # Website configuration interface
│   │   ├── scheduler_dialog.py # Scheduling configuration dialog
│   │   └── settings_panel.py   # Application settings panel
│   ├── scraping/               # Core scraping functionality
│   │   ├── scraper_engine.py   # Main scraping engine
│   │   ├── content_extractor.py # HTML content extraction
│   │   └── output_manager.py   # Data output handling
│   ├── scheduling/             # Task scheduling system
│   │   ├── schedule_manager.py # Main scheduling manager (implemented)
│   │   └── task_scheduler.py   # Simple task scheduler (implemented)
│   └── utils/                  # Utility functions
│       ├── config_manager.py   # JSON configuration handling (implemented)
│       ├── file_handler.py     # File operations utilities
│       └── logger.py           # Logging utilities
├── tests/                      # Test suite
├── data/                       # Configuration and data storage
│   ├── websites.json           # Website configurations
│   ├── schedules.db            # SQLite scheduling database
│   └── logs/                   # Application logs
├── output/                     # Scraped data output directory
│   └── scraped_data/
├── requirements.txt            # Python dependencies
├── main.py                     # Application entry point
├── pytest.ini                 # Test configuration
└── README.md
```

## Technology Stack

### Core Technologies
- **Language**: Python 3.8+
- **GUI Framework**: Tkinter (built-in)
- **Web Scraping**: requests + BeautifulSoup4
- **Scheduling**: schedule library (implemented)
- **Data Storage**: JSON configuration files + SQLite
- **Testing**: pytest framework

### Dependencies
```python
# Current dependencies
schedule>=1.2.0
pytest>=6.0.0

# Required dependencies
requests>=2.28.0
beautifulsoup4>=4.11.0
selenium>=4.0.0  # Optional for JavaScript support

# Built-in libraries
tkinter          # GUI framework
sqlite3          # Database operations
threading        # Background processing
json             # Configuration management
```

## User Interface Design

### Main Window Layout
- **Menu Bar**: File, Edit, Tools, Help
- **Toolbar**: Quick access buttons (Add Site, Start Scraping, Settings)
- **Website List**: Scrollable list of configured websites
- **Status Bar**: Current operation status and last update time
- **Action Buttons**: Start, Stop, Schedule, Configure

### Website Configuration Dialog
- **URL Input**: Website URL with validation
- **Scraping Rules**: CSS selectors or XPath expressions
- **Output Settings**: File format and save location
- **Advanced Options**: Headers, delays, authentication

### Scheduler Interface
- **Frequency Selection**: Dropdown for common intervals
- **Custom Timing**: Time picker for specific schedules
- **Calendar View**: Visual schedule representation
- **Task Status**: Active, paused, or completed tasks

## Development Guidelines

### Code Style Standards
- **PEP 8**: Follow Python Enhancement Proposal 8 for code style
- **Type Hints**: Use type annotations for all function parameters and return values
- **Docstrings**: Google-style docstrings for all classes and functions
- **Line Length**: Maximum 88 characters (Black formatter standard)
- **Import Organization**: Use isort for consistent import ordering

### File Organization
- **Module Structure**: Each module should have a single responsibility
- **Class Design**: Use classes for stateful components, functions for utilities
- **Error Handling**: Comprehensive try-catch blocks with specific exception types
- **Configuration**: Centralized configuration management through `config_manager.py`

### Naming Conventions
- **Variables**: `snake_case` for variables and functions
- **Classes**: `PascalCase` for class names
- **Constants**: `UPPER_CASE` for constants
- **Private Members**: Single underscore prefix for internal use
- **Files**: `snake_case.py` for module files

## Codex Integration Instructions

### Current Implementation Focus
When working on this project, prioritize these areas:

1. **GUI Development**: Implement Tkinter components with modern styling
2. **Web Scraping Engine**: Build robust scraping functionality with error handling
3. **Scheduling System**: Enhance the existing schedule manager with persistence
4. **Configuration Management**: Extend JSON-based configuration system
5. **Testing**: Maintain comprehensive test coverage for all components

### Code Generation Guidelines
- **Always include type hints** for function parameters and return values
- **Generate comprehensive docstrings** using Google style format
- **Include error handling** for all external operations (web requests, file I/O)
- **Follow the existing module structure** and import patterns
- **Generate corresponding tests** for all new functionality

### Implementation Patterns

#### GUI Components
```python
"""Example GUI component structure."""
import tkinter as tk
from tkinter import ttk, messagebox
from typing import Optional, Callable, Dict, Any

class ComponentName:
    """Brief description of the component."""
    
    def __init__(self, parent: tk.Widget, callback: Optional[Callable] = None):
        """Initialize the component.
        
        Args:
            parent: Parent widget
            callback: Optional callback function for events
        """
        self.parent = parent
        self.callback = callback
        self.frame = ttk.Frame(parent)
        self._setup_ui()
    
    def _setup_ui(self) -> None:
        """Set up the user interface components."""
        # Create modern-looking widgets with proper styling
        self.frame.grid(sticky="nsew", padx=10, pady=10)
        
        # Add responsive behavior
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
    
    def show_error(self, message: str) -> None:
        """Display user-friendly error message."""
        messagebox.showerror("Error", message)
    
    def show_success(self, message: str) -> None:
        """Display success message."""
        messagebox.showinfo("Success", message)
```

#### Web Scraping Components
```python
"""Example scraping component structure."""
import requests
from bs4 import BeautifulSoup
from typing import Dict, List, Optional, Any
import logging
import time

logger = logging.getLogger(__name__)

class ScrapingComponent:
    """Brief description of the scraping component."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize with configuration.
        
        Args:
            config: Scraping configuration dictionary
        """
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': config.get('user_agent', 'Cinder Web Scraper 1.0')
        })
        self.delay = config.get('delay', 1)
    
    def scrape(self, url: str) -> Optional[Dict[str, Any]]:
        """Scrape data from the given URL.
        
        Args:
            url: URL to scrape
            
        Returns:
            Scraped data dictionary or None if failed
            
        Raises:
            requests.RequestException: If request fails
        """
        try:
            # Respect rate limiting
            time.sleep(self.delay)
            
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            
            return self._extract_data(response.text)
            
        except requests.RequestException as e:
            logger.error(f"Request failed for {url}: {e}")
            return None
        except Exception as e:
            logger.error(f"Unexpected error scraping {url}: {e}")
            return None
    
    def _extract_data(self, html: str) -> Dict[str, Any]:
        """Extract data from HTML content."""
        soup = BeautifulSoup(html, 'html.parser')
        
        # Extract data based on configuration
        data = {}
        
        # Add extraction logic here
        
        return data
```

#### Configuration Management
```python
"""Example configuration usage."""
from src.utils.config_manager import load_config, save_config
from typing import Dict, Any

def get_scraping_config() -> Dict[str, Any]:
    """Load scraping configuration with defaults."""
    config = load_config("data/config.json")
    
    # Set default values if not present
    if "scraping" not in config:
        config["scraping"] = {
            "default_delay": 1,
            "max_retries": 3,
            "timeout": 30,
            "user_agent": "Cinder Web Scraper 1.0"
        }
        save_config(config, "data/config.json")
    
    return config["scraping"]
```

## Key Requirements

### Functional Requirements
1. **Website Management**
   - Add/remove websites from scraping list
   - Edit scraping configurations
   - Test scraping rules before saving

2. **Scheduled Scraping**
   - Set up recurring scraping tasks
   - Modify existing schedules
   - Start/stop scheduled operations

3. **Data Export**
   - Save scraped data to user-specified paths
   - Support multiple output formats
   - Organize files by date/website

4. **Error Handling**
   - Graceful handling of network errors
   - Retry mechanisms for failed requests
   - Comprehensive logging system

### Non-Functional Requirements
1. **Performance**
   - Efficient memory usage during scraping
   - Responsive GUI during operations
   - Minimal CPU usage when idle

2. **Reliability**
   - Persistent storage of configurations
   - Automatic recovery from crashes
   - Backup of important data

3. **Usability**
   - Intuitive interface for non-technical users
   - Clear error messages and feedback
   - Comprehensive help documentation

## Installation and Setup

### System Requirements
- **Operating System**: Windows 10/11
- **Python Version**: 3.8 or higher
- **Memory**: Minimum 4GB RAM
- **Storage**: 100MB for application, additional for scraped data

### Installation Steps
1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Current Task Context

### Immediate Development Priorities
1. **Implement ScraperEngine**: Create the core web scraping functionality
2. **Build GUI Components**: Develop the main window and dialog interfaces
3. **Enhance Scheduling**: Add persistence to the scheduling system
4. **Add Content Extraction**: Implement BeautifulSoup-based content extraction
5. **Create Output Management**: Build flexible data output system

### Active Development Areas
- **GUI Framework**: Tkinter interface development
- **Web Scraping**: requests + BeautifulSoup4 implementation
- **Data Persistence**: SQLite database integration for schedules
- **Error Handling**: Comprehensive error management system
- **Testing**: Expand test coverage for all modules

## Testing Strategy

### Unit Testing
- **Individual Component Testing**: Test each module in isolation
- **Mock External Dependencies**: Use unittest.mock for external services
- **Automated Test Suite**: Run tests with pytest

### Integration Testing
- **GUI Component Interaction**: Test interface workflows
- **Database Operations**: Test SQLite operations
- **File System Operations**: Test file handling and storage

### User Acceptance Testing
- **Real-world Scraping Scenarios**: Test with actual websites
- **Performance Under Load**: Test with multiple concurrent scrapers
- **Cross-platform Compatibility**: Focus on Windows compatibility

### Testing Patterns
```python
"""Example test structure."""
import pytest
from unittest.mock import Mock, patch, MagicMock
from src.module.component import Component

class TestComponent:
    """Test suite for Component class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        self.component = Component()
    
    def test_functionality(self):
        """Test specific functionality."""
        # Test implementation
        result = self.component.method()
        assert result == expected_result
    
    @patch('src.module.component.requests.get')
    def test_with_mock(self, mock_get):
        """Test with mocked external dependencies."""
        mock_response = MagicMock()
        mock_response.text = "<html>test</html>"
        mock_response.status_code = 200
        mock_get.return_value = mock_response
        
        result = self.component.scrape("http://example.com")
        assert result is not None
```

### Coverage Requirements
- **Minimum Coverage**: 80% overall test coverage
- **Critical Paths**: 100% coverage for core scraping and scheduling logic
- **Error Handling**: Test all exception paths and edge cases
- **GUI Testing**: Test user interaction flows and error scenarios

## Development Phases

### Phase 1: Core Foundation (Current)
- ✅ Basic GUI framework setup
- ✅ Simple scheduling functionality
- ✅ Configuration file management
- 🔄 Web scraping engine implementation

### Phase 2: Enhanced Features
- Scheduling system with SQLite persistence
- Advanced scraping options (headers, delays)
- Error handling and comprehensive logging
- GUI improvements and user feedback

### Phase 3: Polish and Testing
- User interface improvements
- Comprehensive testing suite
- Documentation and help system
- Performance optimization

### Phase 4: Advanced Features
- JavaScript support with Selenium
- Data visualization of scraped content
- Export to databases
- Plugin system for custom extractors

## Error Handling Standards

### Exception Management
```python
"""Standard error handling pattern."""
import logging
from typing import Optional

logger = logging.getLogger(__name__)

def safe_operation(param: str) -> Optional[str]:
    """Perform operation with comprehensive error handling."""
    try:
        # Operation code
        result = perform_operation(param)
        return result
    except ValueError as e:
        logger.error(f"Invalid parameter in operation: {e}")
        return None
    except requests.RequestException as e:
        logger.error(f"Network error in operation: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error in operation: {e}")
        return None
```

### User-Friendly Error Messages
- **Clear Language**: Use non-technical language for user-facing errors
- **Actionable Information**: Provide steps to resolve issues
- **Logging**: Log detailed technical information for debugging
- **Graceful Degradation**: Continue operation when possible

## Security Considerations

### Data Protection
- **Secure Storage**: Encrypt sensitive authentication credentials
- **Input Validation**: Validate all user inputs to prevent injection attacks
- **Safe File Operations**: Use secure file handling practices
- **Resource Cleanup**: Proper cleanup after operations

### Web Scraping Ethics
- **Robots.txt Compliance**: Respect robots.txt files
- **Rate Limiting**: Implement respectful request timing
- **User Education**: Educate users about legal scraping practices
- **Terms of Service**: Respect website terms of service

### Error Prevention
- **Input Validation**: Validate URLs and CSS selectors
- **Safe File Handling**: Prevent directory traversal attacks
- **Resource Management**: Proper cleanup of network resources

## Performance Optimization

### GUI Performance
- **Responsive Design**: Use threading for long-running operations
- **Memory Management**: Efficient widget creation and destruction
- **Resource Cleanup**: Proper cleanup of GUI resources
- **Progress Feedback**: Visual progress indicators for user operations

### Scraping Performance
- **Rate Limiting**: Implement respectful request timing
- **Connection Pooling**: Reuse HTTP connections when possible
- **Caching**: Cache scraped data to reduce redundant requests
- **Parallel Processing**: Use threading for multiple site scraping

### Data Management
- **Efficient Storage**: Optimize JSON and SQLite operations
- **File Handling**: Stream large files to minimize memory usage
- **Cleanup**: Automatic cleanup of old scraped data
- **Compression**: Compress stored data when appropriate

## Documentation Requirements

### User Documentation
- **Installation Guide**: Step-by-step setup instructions
- **User Manual**: Comprehensive usage documentation with screenshots
- **Troubleshooting Guide**: Common issues and solutions
- **FAQ Section**: Frequently asked questions and answers

### Developer Documentation
- **Code Documentation**: Docstrings and comments for all functions
- **API Reference**: Complete API documentation
- **Architecture Overview**: High-level system design
- **Contributing Guidelines**: How to contribute to the project

## Monitoring and Logging

### Logging Strategy
```python
"""Logging configuration example."""
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('data/logs/scraper.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
```

### Performance Monitoring
- **Operation Timing**: Track scraping operation duration
- **Resource Usage**: Monitor memory and CPU usage
- **Error Rates**: Track and alert on error frequency
- **User Activity**: Log user interactions for UX improvement

## Future Enhancements

### Planned Features
- **Cloud Storage Integration**: AWS S3, Google Drive, Dropbox
- **Mobile Companion App**: Remote monitoring and control
- **Machine Learning**: Automatic content detection and extraction
- **Browser Extension**: Quick website adding from browser
- **Multi-language Support**: Internationalization support
- **Advanced Data Processing**: Filtering, transformation, analysis

### Potential Integrations
- **Database Connections**: MySQL, PostgreSQL, MongoDB
- **Cloud Services**: AWS, Google Cloud, Azure
- **Notification Systems**: Email, SMS, Slack
- **Data Analysis Tools**: pandas, matplotlib, jupyter

## Success Metrics

### User Experience
- **Ease of Setup**: Time to first successful scrape
- **Configuration Reliability**: Success rate of scraping configurations
- **Operation Speed**: Average scraping time per website
- **Data Quality**: Accuracy of extracted data

### Technical Performance
- **Memory Usage**: Optimize for efficient memory consumption
- **Error Rate**: Minimize scraping failures and crashes
- **System Stability**: Maintain 99%+ uptime during operations
- **Data Integrity**: Ensure 100% data accuracy and consistency

---

*This agents.md file serves as the comprehensive specification for the Cinder's Web Scraper project. It should be updated as requirements evolve and new features are implemented. This document guides both human developers and AI agents in understanding the project structure, requirements, and development standards.*
