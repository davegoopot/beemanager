# beemanager
Tools for managing bee hives

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Building and Deployment](#building-and-deployment)
  - [Automated Deployment with GitHub Actions](#automated-deployment-with-github-actions)
- [Development](#development)
- [Django Web Interface](#django-web-interface)
- [Camera](#camera)

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

### Automated Deployment with GitHub Actions

The repository includes a GitHub Actions workflow that automatically deploys to a local server when tests pass on the `main` branch. 

#### Setting Up GitHub Secrets for Deployment

To enable automated deployment, you need to configure the following secrets in your GitHub repository settings:

1. **Navigate to Repository Settings**:
   - Go to your GitHub repository
   - Click on "Settings" tab
   - In the left sidebar, click "Secrets and variables" → "Actions"

2. **Add Required Secrets**:

   | Secret Name | Description | Example |
   |-------------|-------------|---------|
   | `DEPLOY_SSH_KEY` | Private SSH key for server access | `-----BEGIN OPENSSH PRIVATE KEY-----...` |
   | `DEPLOY_HOST` | Server hostname or IP address | `192.168.1.100` or `myserver.local` |
   | `DEPLOY_USER` | Username for SSH connection | `pi` or `ubuntu` |
   | `DEPLOY_PATH` | Target directory on server | `/home/pi/beemanager` |

3. **SSH Key Setup**:
   
   Generate an SSH key pair on your local machine:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "github-actions-deploy"
   ```
   
   Copy the public key to your server:
   ```bash
   ssh-copy-id -i ~/.ssh/id_rsa.pub user@your-server
   ```
   
   Add the **private key** content to the `DEPLOY_SSH_KEY` secret in GitHub.

4. **Server Preparation**:
   
   Ensure your target server has:
   - Python 3.13+ installed
   - UV package manager installed (`pip install uv`)
   - Target directory created with proper permissions
   - SSH access enabled

#### Deployment Process

The automated deployment workflow:

1. **Triggers** on pushes to `main` branch
2. **Runs Tests** to ensure code quality
3. **Builds** the project using `uv build`
4. **Transfers** built artifacts to the server via SCP
5. **Installs** the updated package on the server
6. **Runs** Django migrations and collects static files

#### Manual Deployment Trigger

You can also trigger deployment manually from the GitHub Actions tab in your repository by running the "Deploy to Local Server" workflow.

#### Troubleshooting Deployment

- **SSH Connection Issues**: Verify your SSH key and server details
- **Permission Errors**: Ensure the deploy user has write access to the target directory
- **Build Failures**: Check that all tests pass before deployment
- **Server Errors**: Review the deployment logs in GitHub Actions for detailed error messages

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