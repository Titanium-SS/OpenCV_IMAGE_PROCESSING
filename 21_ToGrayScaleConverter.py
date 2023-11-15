# This code was not part of the Video Seriesi

import cv2
import os

# Path to the folder containing the images
input_folder = "negatives"

# Path to the folder where the processed images will be saved
output_folder = "neg"

# Keep track of the number of processed images
count = 1

# Loop through each file in the input folder
for filename in os.listdir(input_folder):
    # Read the image
    img = cv2.imread(os.path.join(input_folder, filename))

    # Resize the image
    resized_img = cv2.resize(img, (500, 250))

    # Convert the image to grayscale
    grayscale_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    # Save the processed image to the output folder with a sequential filename
    output_filename = "image{}.jpg".format(count)
    cv2.imwrite(os.path.join(output_folder, output_filename), grayscale_img)

    # Increment the counter
    count += 1
    