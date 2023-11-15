"""
This code is segmenting the foreground object in an image using the GrabCut algorithm. 
The foreground object is defined as the region inside the specified rectangle. 
The result is a new image where all background pixels have been set to zero (black).
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('images/cod1.png')
mask = np.zeros(img.shape[:2], np.uint8)

bgdModel = np.zeros((1,65), np.float64)
fgdModel = np.zeros((1,65), np.float64)

rect = (100, 100, 750, 750)   # change the values of dimensions of rectangle argument

cv2.grabCut(img, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()