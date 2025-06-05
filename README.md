# beemanager
Tools for managing bee hives

## Django Web Interface

The project now includes a basic Django web application that serves a Hello-World style page. To run the web interface:

```bash
# Install dependencies
uv sync

# Run the Django development server
uv run python manage.py runserver

# Or run on a specific port
uv run python manage.py runserver 0.0.0.0:8000
```

The web interface will be available at http://localhost:8000 and displays a bee-themed hello world page.

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