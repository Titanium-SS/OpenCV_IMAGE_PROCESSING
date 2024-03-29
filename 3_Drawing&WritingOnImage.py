"""
this code reads an image, draws a line, a rectangle, a circle, 
and a polygon on it, writes some text, and displays the result. 
The process continues until a key is pressed.
"""

import cv2
import numpy as np 

img = cv2.imread('images/IMAGE1.jpg', cv2.IMREAD_COLOR)

#DRAWING
    ### the color scheme in cv2 is :    B    G    R     Linewidth(optional)
cv2.line(img, (0,0), (100,100),   (255, 255, 255),          15)

cv2.rectangle(img, (15,25), (200,150), (0, 255, 0),          5)

cv2.circle(img, (500,300), 55, (255, 0, 0),                 -1)         #-1 fills the circle


    ### DRAWING A POLYGON
pts = np.array([[600,200],[500,70],[70,20],[50,10]], np.int32)
    ### pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 55, 255), 5)


#WRITING

font = cv2.FONT_HERSHEY_SIMPLEX                          #size                    #thickness
cv2.putText(img, 'ROGER THAT SERGEANT', (100,350), font,     1   , (200, 255, 100),     2      , cv2.LINE_AA)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
