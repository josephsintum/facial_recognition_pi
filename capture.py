from io import BytesIO
from time import sleep
from picamera import PiCamera

# Create the in-memory stream
stream = BytesIO()
camera = PiCamera()
# camera.start_preview()
sleep(2)

with PiCamera() as camera:
    # camera.start_preview()
    try:
        for i, filename in enumerate(
                camera.capture_continuous('image{counter:02d}.jpg')):
            print(filename)
            time.sleep(0.5)
            if i == 32:
                break

    # finally:
    #     camera.stop_preview()
