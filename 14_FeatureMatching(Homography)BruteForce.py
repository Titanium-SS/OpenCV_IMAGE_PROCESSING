"""
This code reads two images, detects keypoints and computes descriptors for both images, 
matches the descriptors, draws the best matches, and displays the result. 
The process continues until a key is pressed.
"""
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('Img14A.jpg', 1)
img2 = cv2.imread('Img14C.jpg', 1)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches[:10], None, flags=2)

plt.imshow(img3)
plt.show()