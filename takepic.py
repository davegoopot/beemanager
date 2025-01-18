"""
    Simple script to take a picture with the Raspberry Pi camera. Intended to be run using 
    `uv run takepic.py` from the command line.
"""

import os
import picamera2

def take_picture(filname: str):
    camera = picamera2.Picamera2()
    still_config = camera.create_still_configuration(main={"size": (640, 480)})
    camera.configure(still_config)
    camera.start()
    camera.capture_file(filename)
    print(f'Image saved as {filename}')
    camera.close()

if __name__ == "__main__":
    picture_folder = "pics"
    os.makedirs(picture_folder, exist_ok=True)
    filename = os.path.join(picture_folder, "testimage.jpg")
    take_picture(filename)