# beemanager
Tools for managing bee hives

## Prerequisites

- Python 3.13 or higher
- [UV](https://docs.astral.sh/uv/) package manager
- For camera functionality: Raspberry Pi with camera module and picamera2 library

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

4. **For camera functionality**, install additional dependencies on Raspberry Pi:
   ```bash
   uv pip install picamera2
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

### Running the Camera Module

On a Raspberry Pi with camera module:

```bash
uv run python burst.py
```

This will take 10 pictures and save them in the `pics/` directory.

## Camera

An initial objective is to set up a system that will take pictures of the entrance of a bee hive at
regular intervals. The pictures will be used to monitor the activity of the hive. The pictures should
be accessible remotely from a mobile device.

### Initial Camera Experiment

As an initial experiment, I will set up a Raspberry Pi with a camera to take pictures on a regular
schedule using cron. The pictures will be stored on the Raspberry Pi and only accessible with SSH
access to the Pi.

### Usage

The camera module can be used programmatically:

```python
from burst import Burster

# Create a burster instance
burster = Burster(pics_folder="my_pics")

# Take a single picture
burster.take_pictures(1)

# Take multiple pictures
burster.take_pictures(5)
```