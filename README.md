# beemanager
Tools for managing bee hives

## Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) package manager

## Installation

1. Install UV if not already installed:
   ```bash
   pip install uv
   ```

2. Clone the repository:
   ```bash
   git clone https://github.com/davegoopot/beemanager.git
   cd beemanager
   ```

3. Set up the development environment:
   ```bash
   uv sync
   ```

## Building and Deployment

### Building the Project

Create a source distribution and wheel for deployment:

```bash
uv build
```

This creates two files in the `dist/` directory:
- `burst-0.1.0.tar.gz` (source distribution)
- `burst-0.1.0-py3-none-any.whl` (wheel)

### Deployment to Target Machine

1. **Copy the distribution files** to your target machine (e.g., Raspberry Pi):
   ```bash
   scp dist/burst-0.1.0.tar.gz user@target-machine:/path/to/deployment/
   ```

2. **On the target machine**, install UV if not present:
   ```bash
   pip install uv
   ```

3. **Install the package** from the source distribution:
   ```bash
   uv pip install burst-0.1.0.tar.gz
   ```

   Or install from the wheel:
   ```bash
   uv pip install burst-0.1.0-py3-none-any.whl
   ```

### Alternative: Direct Installation from Repository

For development or testing, you can install directly from the repository:

```bash
uv pip install git+https://github.com/davegoopot/beemanager.git
```

## Development

### Running Tests

Run the test suite to verify functionality:

```bash
uv run pytest
```

## Django Web Interface

The project now includes a basic Django web application that serves a Hello-World style page. To run the web interface:

```bash
# Install dependencies
uv sync

# Run the Django development server
uv run python manage.py runserver

# Or run on a specific port
uv run python manage.py runserver 0.0.0.0:8000

# Or use the convenience script to run on bee-themed port 8335
. serve.bash
```

The web interface will be available at http://localhost:8000 (or http://localhost:8335 when using `serve.bash`) and displays a bee-themed hello world page.

### Django Features

- **No Database Configuration**: Uses Django's dummy database backend, so no database setup is required
- **Simple Hello World Page**: Displays a bee-themed welcome message
- **Minimal Setup**: Basic Django project structure without unnecessary complexity

## Camera

An initial objective is to set up a system that will take pictures of the entrance of a bee hive at
regular intervals. The pictures will be used to monitor the activity of the hive. The pictures should
be accessible remotely from a mobile device.

### Initial Camera Experiment

As an initial experiment, I will set up a Raspberry Pi with a camera to take pictures on a regular
schedule using cron. The pictures will be stored on the Raspberry Pi and only accessible with SSH
access to the Pi.