import numpy as np
import cv2

# set for default camera
# cap = cv2.VideoCapture(0)

# set 2 for certain cameras
cap = cv2.VideoCapture(2)
cap.set(3, 800)  # set width
cap.set(4, 600)  # set height

while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1) # Flip camera vertically
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
    
cap.release()
cv2.destroyAllWindows()