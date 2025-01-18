"""
    Simple script to take a picture with the Raspberry Pi camera. Intended to be run using 
    `uv run takepic.py` from the command line.

    To make the uv dependencies work, we add inline script metadata.
"""

# /// script
# dependencies = [
#   "picamera"
# ]
# ///

import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
filename = 'testimage.jpg'
camera.capture(filename)
print(f'Image saved as {filename}')
