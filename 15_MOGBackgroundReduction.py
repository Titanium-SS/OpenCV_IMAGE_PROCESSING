"""
This code captures video from a webcam, applies a background subtraction method to separate 
moving objects from the static background, and displays the original and processed video. 
The process continues until the ‘q’ key is pressed.
"""

import cv2

cap = cv2.VideoCapture(0)
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)

    cv2.imshow('original', frame)
    cv2.imshow('fg', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()