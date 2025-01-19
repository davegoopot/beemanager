"""
    pytest file for developing the photo burst functions.
"""
import os
from burst import Burster
from datetime import datetime

def test_givenImageCountOne_takeOnePicture():
    dummy_camera = DummyCamera()
    burster = Burster(dummy_camera, pics_folder="pics")
    burster.take_pictures()
    assert dummy_camera.picture_count == 1
    assert len(dummy_camera.picture_filenames) == 1
    # pic_20250119_1424_123.jpg
    assert dummy_camera.picture_filenames[0].startswith(os.path.join("pics", "pic_"))   
    assert dummy_camera.picture_filenames[0].endswith(".jpg")
    assert dummy_camera.picture_filenames[0].split("_")[1] == datetime.now().strftime("%Y%m%d")



class DummyCamera:
    picture_count = 0
    picture_filenames = []

    def capture_file(self, filename):
        self.picture_count += 1
        self.picture_filenames.append(filename)

    def close(self):
        pass

    def create_still_configuration(self, main):
        pass

    def configure(self, config):
        pass

    def start(self):
        pass