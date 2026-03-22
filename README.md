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

## Running As a Linux Service

To run the Django development server automatically on server reboot, you can set up a systemd service:

1. Create a systemd service file:
   ```bash
   sudo tee /etc/systemd/system/serve.service > /dev/null << 'EOF'
   [Unit]
   Description=Django Development Server
   After=network.target

   [Service]
   Type=simple
   User=dave
   WorkingDirectory=/home/dave/beemanager
   ExecStart=/bin/bash /home/dave/beemanager/serve.bash
   Restart=always
   RestartSec=5s

   [Install]
   WantedBy=multi-user.target
   EOF
   ```

2. Reload systemd to recognize the new service:
   ```bash
   sudo systemctl daemon-reload
   ```

3. Enable the service to start automatically on boot:
   ```bash
   sudo systemctl enable serve.service
   ```

4. Start the service immediately:
   ```bash
   sudo systemctl start serve.service
   ```

5. Verify the service is running:
   ```bash
   sudo systemctl is-active serve.service
   sudo systemctl is-enabled serve.service
   ```

> The Django development server will now start automatically when the system boots and restart automatically if it crashes

## Serving Over Tailscale

```bash
sudo tailscale serve --bg http://localhost:8335
```

