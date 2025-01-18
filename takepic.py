"""
    Simple script to take a picture with the Raspberry Pi camera. Intended to be run using 
    `uv run takepic.py` from the command line.
"""

try:
    import picamera2
except Exception as ex:
    print(ex)

camera = picamera2.Picamera2()
still_config = camera.create_still_configuration(main={"size": (640, 480)})
camera.configure(still_config)
camera.start()
filename = 'testimage.jpg'
camera.capture_file(filename)
print(f'Image saved as {filename}')
