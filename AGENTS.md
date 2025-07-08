# Cinder's Web Scraper - Agent Specification

## Project Overview

A GUI-based web scraper application for Windows systems built with Python. The application enables users to configure, schedule, and manage web scraping tasks through an intuitive interface.

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

### File Structure

```
cinder-webscraper/
├── src/
│   ├── gui/
│   │   ├── main_window.py
│   │   ├── website_manager.py
│   │   ├── scheduler_dialog.py
│   │   └── settings_panel.py
│   ├── scraping/
│   │   ├── scraper_engine.py
│   │   ├── content_extractor.py
│   │   └── output_manager.py
│   ├── scheduling/
│   │   ├── task_scheduler.py
│   │   └── schedule_manager.py
│   └── utils/
│       ├── config_manager.py
│       ├── file_handler.py
│       └── logger.py
├── data/
│   ├── websites.json
│   ├── schedules.db
│   └── logs/
├── output/
│   └── scraped_data/
├── requirements.txt
├── main.py
└── README.md
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

## Key Requirements

### Functional Requirements

1. Website Management
   - Add/remove websites from scraping list
   - Edit scraping configurations
   - Test scraping rules before saving
2. Scheduled Scraping
   - Set up recurring scraping tasks
   - Modify existing schedules
   - Start/stop scheduled operations
3. Data Export
   - Save scraped data to user-specified paths
   - Support multiple output formats
   - Organize files by date/website
4. Error Handling
   - Graceful handling of network errors
   - Retry mechanisms for failed requests
   - Comprehensive logging system

### Non-Functional Requirements

1. Performance
   - Efficient memory usage during scraping
   - Responsive GUI during operations
   - Minimal CPU usage when idle
2. Reliability
   - Persistent storage of configurations
   - Automatic recovery from crashes
   - Backup of important data
3. Usability
   - Intuitive interface for non-technical users
   - Clear error messages and feedback
   - Comprehensive help documentation

## Installation and Setup

### System Requirements

- **Operating System**: Windows 10/11
- **Python Version**: 3.8 or higher
- **Memory**: Minimum 4GB RAM
- **Storage**: 100MB for application, additional for scraped data

### Dependencies

```
requests>=2.28.0
beautifulsoup4>=4.11.0
schedule>=1.2.0
tkinter (built-in)
sqlite3 (built-in)
threading (built-in)
json (built-in)
```

### Installation Steps

1. Clone the repository
2. Install required packages: `pip install -r requirements.txt`
3. Run the application: `python main.py`

## Development Phases

### Phase 1: Core Foundation

- Basic GUI framework setup
- Simple web scraping functionality
- Configuration file management

### Phase 2: Enhanced Features

- Scheduling system implementation
- Advanced scraping options
- Error handling and logging

### Phase 3: Polish and Testing

- User interface improvements
- Comprehensive testing
- Documentation and help system

### Phase 4: Advanced Features

- JavaScript support with Selenium
- Data visualization of scraped content
- Export to databases
- Plugin system for custom extractors

## Security Considerations

### Data Protection

- Secure storage of authentication credentials
- Encryption of sensitive configuration data
- Safe handling of user input

### Web Scraping Ethics

- Respect robots.txt files
- Implement rate limiting
- User education about legal scraping practices

### Error Prevention

- Input validation for URLs and selectors
- Safe file handling practices
- Resource cleanup after operations

## Testing Strategy

### Unit Testing

- Individual component testing
- Mock external dependencies
- Automated test suite

### Integration Testing

- GUI component interaction
- Database operations
- File system operations

### User Acceptance Testing

- Real-world scraping scenarios
- Performance under load
- Cross-platform compatibility (Windows focus)

## Documentation Requirements

### User Documentation

- Installation guide
- User manual with screenshots
- Troubleshooting guide
- FAQ section

### Developer Documentation

- Code documentation and comments
- API reference
- Architecture overview
- Contributing guidelines

## Future Enhancements

### Planned Features

- Cloud storage integration
- Mobile companion app
- Machine learning for content detection
- Browser extension for quick website adding
- Multi-language support
- Advanced data filtering and processing

### Potential Integrations

- Database connections (MySQL, PostgreSQL)
- Cloud services (AWS, Google Cloud)
- Notification systems (email, SMS)
- Data analysis tools (pandas, matplotlib)

## Success Metrics

### User Experience

- Ease of setup and configuration
- Reliability of scheduled operations
- Speed of scraping operations
- Quality of extracted data

### Technical Performance

- Memory usage optimization
- Error rate minimization
- System stability
- Data integrity maintenance

------

*This specification serves as the foundation for the Cinder's Web Scraper project. It should be updated as requirements evolve and new features are implemented.*