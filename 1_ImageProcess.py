import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('IMAGE1.jpg', cv2.IMREAD_GRAYSCALE)

# IMREAD_COLOR = 1
# IMREAD_UNCHANGED = -1

# Below code opens the image in a python window - movable, closed by pressing any key
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
#Below code opens image in matplotlib window (coordinated)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([330,40], [310,120], 'r', linewidth=5)
plt.show()
"""

cv2.imwrite('cod1.png', img)
