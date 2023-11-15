"""
1. Creating Positive and Negative Images: The function create_positive_and_negative_images() is 
used to create positive and negative images. It iterates over the images in the ‘negative_images’ directory, 
and for each image, it writes a line to the ‘background_images.text’ file with the path of the image. 
If the images were of type ‘positive_images’, it would write a line to the ‘info.dat’ file with the path of the image and additional information.

2. Removing Unwanted Images: The function remove_unwanted_images() is used to remove unwanted images 
from the ‘negative_images’ directory. It iterates over the images in the ‘negative_images’ directory 
and for each image, it compares it with all the images in the ‘unwanted_images’ directory. 
If it finds a match (i.e., the images are identical), it removes the image from the ‘negative_images’ directory.

"""


import urllib.request
import cv2
import numpy as np
import os

def remove_unwanted_images():
    for image_type in ['negative_images']:
        for image in os.listdir(image_type):
            for unwanted in os.listdir('unwanted_images'):
                try:
                    current_image_path = str(image_type) + '/' + str(image)
                    unwanted_image = cv2.imread('unwanted_images/' + str(unwanted))
                    target_image = cv2.imread(current_image_path)

                    if unwanted_image.shape == target_image.shape and not (np.bitwise_xor(unwanted_image, target_image).any()):
                        print('Unwanted Image Found')
                        print(current_image_path)
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

def create_positive_and_negative_images():
    for image_type in ['negative_images']:
        for image in os.listdir(image_type):
            if image_type == 'negative_images':
                line = image_type+'/'+image+'\n'
                with open('background_images.text', 'a') as f:
                    f.write(line)

            elif image_type == 'positive_images':
                line = image_type+'/'+image+' 1 0 0 50 50\n'
                with open('info.dat', 'a') as f:
                    f.write(line)

create_positive_and_negative_images()
remove_unwanted_images()
