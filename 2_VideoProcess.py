"""
This code captures video from a webcam, displays it, converts it to grayscale, 
displays the grayscale video, and saves the original video to a file. 
The process continues until the ‘q’ key is pressed.
"""


import cv2
import numpy as np 

cap = cv2.VideoCapture(0)
#Output the file - codec to be used
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output1.avi', fourcc, 20.0, (640, 480))

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    out.write(frame)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
