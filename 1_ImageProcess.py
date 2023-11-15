"""
This code reads an image, converts it to grayscale, displays it, and then saves the grayscale image to a new file. 
The commented code, if uncommented, would also display the image with a red line using Matplotlib.
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/IMAGE1.jpg', cv2.IMREAD_GRAYSCALE)

# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# Below code opens the image in a python window - movable, closed by pressing any key
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Below commented code opens image in matplotlib window (coordinated)

"""
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([330,40], [310,120], 'r', linewidth=5)
plt.show()
"""

cv2.imwrite('cod1.png', img)
