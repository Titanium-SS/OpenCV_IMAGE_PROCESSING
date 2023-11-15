"""
This code reads two images, adds them together in different ways, displays the result of the weighted addition, 
and contains commented code that, if uncommented, would overlay one image onto another. 
The process continues until a key is pressed.
"""


import cv2
import numpy as np 


img1 = cv2.imread('images/left.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('images/right.jpg', cv2.IMREAD_COLOR)

add = img1 + img2                 # Simply add the images while keeping their opaqueness intact

add = cv2.add(img1, img2)         # Add the color values of the pixel in the area

weighted = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)         # opaqueness can be affected and added in the image so produced

cv2.imshow('AddedImages', weighted)


"""
img2 = cv2.imread('MYLOGO.jpg')
img1 = cv2.imread('imageSRC2.jpg')


rows, cols, channels = img2.shape
roi = img2[0:rows, 0:cols]

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 220, 250, cv2.THRESH_BINARY_INV)


mask_inv = cv2.bitwise_not(mask)    # bitwise = low-level logical operation (AND / OR / NOT / XOR)
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow('res', img1)
cv2.imshow('mask_inv', mask_inv)
cv2.imshow('img1_bg', img1_bg)
cv2.imshow('img2_fg', img2_fg)
cv2.imshow('dst', dst)     



#cv2.imshow('mask', mask)  shows the image with the mask
"""

cv2.waitKey(0)
cv2.destroyAllWindows()
