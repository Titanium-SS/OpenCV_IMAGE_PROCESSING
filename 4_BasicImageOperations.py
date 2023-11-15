"""
This code reads an image, accesses and modifies a specific pixel, 
accesses and modifies a region of the image, 
copies a region of the image to another location,and displays the result. 
The process continues until a key is pressed.
"""


import cv2
import numpy as np 


img = cv2.imread('images/IMAGE1.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]                  #Prints the actual color value of the pixel of image 
print(px)

img[55, 55] = [255, 255, 255]     #Modifies the color value of the pixel of the image
print(px)

roi = img[100:150, 100:150]       #Stands for Region of Image  - gives pixels values of the region
print(roi)

roi = img[100:150, 100:150] = [255, 255, 255]


watch_face = img[50:150, 100:200]
img[0:100, 0:100] = watch_face


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
