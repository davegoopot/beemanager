"""
    Simple script to take a picture with the Raspberry Pi camera. Intended to be run using 
    `uv run takepic.py` from the command line.
"""

from datetime import datetime
import os
import picamera2
from time import sleep

class Burster():
    def __init__(self, camera = None, pics_folder = "pics"):
        self._camera = camera
        if not self._camera:
            self._camera = picamera2.Picamera2()
            still_config = self._camera.create_still_configuration(main={"size": (640, 480)})
            self._camera.configure(still_config)
            self._camera.start()

        self._pics_folder = pics_folder

    def take_pictures(self, num_pics: int = 1):
        for _ in range(num_pics):
            filename = self._make_filename()
            self.take_picture(os.path.join(self._pics_folder, filename))
            sleep(0.1)

        self._camera.close()

    def _make_filename(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M_%S_%f")
        return f"pic_{timestamp}.jpg"


    def take_picture(self, filename: str):
        os.makedirs(os.path.dirname(filename), exist_ok=True)        
        self._camera.capture_file(filename)
        print(f'Image saved as {filename}')
        

if __name__ == "__main__":
    Burster().take_pictures(10)