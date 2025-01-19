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


def test_givenImageCountThree_takeThreePictures():
    dummy_camera = DummyCamera()
    burster = Burster(dummy_camera, pics_folder="pics")
    burster.take_pictures(num_pics = 3)
    assert dummy_camera.picture_count == 3
    assert len(dummy_camera.picture_filenames) == 3



class DummyCamera:
    def __init__(self):
        self.picture_count = 0
        self.picture_filenames = []

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