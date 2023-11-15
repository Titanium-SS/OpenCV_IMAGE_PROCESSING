# This code was not part of the Video Series

import os
from PIL import Image

path = "pos"
dirs = os.listdir(path)

def resize_rename(img_path, output_path, num):
    img = Image.open(img_path).convert('L') # Convert to black and white
    img = img.resize((300, 300)) # Resize image to 300x300
    new_name = str(num) + ".jpg" # Rename file to new sequential number
    img.save(output_path + new_name) # Save new image
    
count = 1
for item in dirs:
    if os.path.isfile(path + item):
        resize_rename(path + item, path, count)
        count += 1
