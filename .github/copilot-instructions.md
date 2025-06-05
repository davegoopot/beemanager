# GitHub Copilot Instructions for BeeManager

## Project Overview
BeeManager is a Python-based tool for managing bee hives, with a focus on monitoring and automation. The project includes camera functionality for monitoring hive entrances and a Django web interface for remote access.

## Technology Stack
- **Python**: 3.13+ (primary language)
- **Django**: 4.2+ (web framework)
- **UV**: Package manager (preferred over pip)
- **Testing**: pytest for unit tests
- **Database**: Django dummy backend (no actual database required)
- **Camera**: picamera2 for Raspberry Pi camera integration
- **Hardware**: Designed for Raspberry Pi deployment

## Project Structure
```
beemanager/
├── core/                    # Django app for web interface
├── django_project/          # Django project configuration
├── tests/                   # pytest unit tests
├── web_tests/              # Django-specific tests
├── burst.py                # Main module
├── manage.py               # Django management commands
└── pyproject.toml          # Project configuration
```

## Development Guidelines

### Code Style
- Follow PEP 8 conventions
- Use descriptive variable names related to beekeeping domain
- Prefer explicit imports over wildcard imports
- Add docstrings for public functions and classes

### Testing
- Use pytest for unit tests (preferred test framework)
- Django tests go in `web_tests/` directory
- Run tests with: `python -m pytest --ignore=tests/test_burst.py`
- Web tests: `python web_tests/test_django_hello.py`

### Dependencies
- Use UV for dependency management: `uv sync`, `uv add package`
- Avoid adding unnecessary dependencies
- Django dummy backend means no database migrations needed

### Django Configuration
- Uses dummy database backend (no real database)
- Minimal Django setup for simple web interface
- Static files handling is basic
- No user authentication system implemented

## Domain Context

### Beekeeping Terminology
- **Hive**: The structure housing a bee colony
- **Colony**: The community of bees living together
- **Brood**: Developing bees (eggs, larvae, pupae)
- **Frames**: Removable structures inside hives
- **Supers**: Hive boxes for honey storage

### Camera Monitoring
- Uses `picamera2` library for Raspberry Pi camera module
- `Burster` class handles picture capture with timestamp filenames
- Regular interval photography of hive entrances
- Pictures stored locally in `pics/` folder (configurable)
- Image format: JPEG, 640x480 resolution
- Remote access via mobile devices (future goal)
- Cron-based scheduling for automated captures

### Hardware Context
- Raspberry Pi deployment target
- Camera module integration
- Network connectivity for remote monitoring
- Power efficiency considerations

## Deployment
- Build with: `uv build`
- Deploy to Raspberry Pi via SCP
- No complex server setup required
- Web interface runs on development server

## Common Patterns
- Use `uv run` prefix for running commands
- Django uses British English locale (en-gb)
- London timezone (Europe/London)
- Timestamp format: `YYYYMMDD_HHMM_SS_microseconds` for filenames
- Directory creation with `os.makedirs(path, exist_ok=True)`
- HTML embedded in Django views for simplicity
- Bee-themed styling with yellow/gold color scheme
- Simple, minimal approach preferred over complex solutions

## Avoid
- Complex database schemas (project uses dummy backend)
- Heavy dependencies that complicate Raspberry Pi deployment
- Authentication systems (not currently needed)
- Complex frontend frameworks (keep it simple)