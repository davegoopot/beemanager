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

### Manual Deployment to Private Repository

To manually deploy the built files to the private deployment repository (`davegoopot/beemanager-deploy`):

#### Prerequisites

1. **Create a Personal Access Token (PAT)** with appropriate permissions:
   - Go to https://github.com/settings/tokens
   - Click "Generate new token" → "Generate new token (classic)"
   - Give it a descriptive name like "Deploy to beemanager-deploy"
   - Set expiration (recommend a long period for automation)
   - Select the `repo` scope (this includes all repository permissions)
   - Click "Generate token"
   - **Copy the token immediately** (it won't be shown again)

2. **Verify token has access** to the deployment repository:
   ```bash
   # Test API access
   curl -H "Authorization: token YOUR_TOKEN" \
        https://api.github.com/repos/davegoopot/beemanager-deploy
   
   # Test git access
   git ls-remote https://YOUR_TOKEN@github.com/davegoopot/beemanager-deploy.git
   ```

#### Deployment Steps

1. **Build the project** (if not already done):
   ```bash
   uv build
   ```

2. **Clone the deployment repository** (or use an existing clone):
   ```bash
   # First time setup
   git clone https://YOUR_TOKEN@github.com/davegoopot/beemanager-deploy.git
   cd beemanager-deploy
   
   # Or if already cloned
   cd beemanager-deploy
   git pull origin main
   ```

3. **Copy the built distribution files**:
   ```bash
   # From the beemanager repository root
   cp ../beemanager/dist/* .
   ```

4. **Commit and push the changes**:
   ```bash
   git add *.tar.gz *.whl
   git commit -m "Deploy beemanager build artifacts"
   git push origin main
   ```

#### Alternative: One-Step Deployment Script

Create a deployment script to automate the manual steps:

```bash
#!/bin/bash
# deploy.sh - Manual deployment script

set -e

# Configuration
DEPLOY_REPO="https://YOUR_TOKEN@github.com/davegoopot/beemanager-deploy.git"
DEPLOY_DIR="/tmp/beemanager-deploy"

echo "Building project..."
uv build

echo "Cloning/updating deployment repository..."
if [ -d "$DEPLOY_DIR" ]; then
  cd "$DEPLOY_DIR"
  git pull origin main
else
  git clone "$DEPLOY_REPO" "$DEPLOY_DIR"
  cd "$DEPLOY_DIR"
fi

echo "Copying build artifacts..."
cp ../beemanager/dist/* .

echo "Committing and pushing..."
git add *.tar.gz *.whl
git commit -m "Deploy beemanager build artifacts - $(date +%Y-%m-%d)"
git push origin main

echo "Deployment complete!"
```

**Usage:**
1. Replace `YOUR_TOKEN` with your actual GitHub Personal Access Token
2. Save as `deploy.sh` and make executable: `chmod +x deploy.sh`
3. Run: `./deploy.sh`

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