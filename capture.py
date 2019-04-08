import time
import picamera

with picamera.PiCamera() as camera:
    camera.start_preview()
    try:
        for i, filename in enumerate(
                camera.capture_continuous('image{counter:02d}.jpg')):
            print(filename)
            time.sleep(0.5)
            if i == 32:
                break
    finally:
        camera.stop_preview()



from io import BytesIO
from time import sleep
from picamera import PiCamera
from PIL import Image

# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.capture(stream, format='jpeg')
# "Rewind" the stream to the beginning so we can read its content
stream.seek(0)
image = Image.open(stream)

image.save("test.jpg","JPEG")