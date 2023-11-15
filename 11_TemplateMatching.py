"""
This code reads an image and a template, performs template matching to find the template in the image, 
draws rectangles at the locations where the template is found, and displays the result. 
The process continues until a key is pressed.
"""


import cv2
import numpy as np

img_bgr = cv2.imread('images/query.png')
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('images/find.png', 0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.6
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0, 255, 255), 2)


cv2.imshow('detected', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

# the yellow edged(boxed) part anywhere in the displayed image is the part where find.png is found on query.png 