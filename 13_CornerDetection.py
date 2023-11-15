"""
This code reads an image, converts it to grayscale, detects corners in the grayscale image,
draws circles at the detected corners, and displays the result. 
The process continues until a key is pressed.
"""

import cv2
import numpy as np

img = cv2.imread('map.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 500, 0.01, 10)  # 500 denotes the no. of corners allowed(come to live) 
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)

cv2.imshow('Corner', img)
cv2.waitKey(0)
cv2.destroyAllWindows()