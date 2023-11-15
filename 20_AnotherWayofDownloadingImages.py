# This code was not part of the Video Series

import os
import requests
from bs4 import BeautifulSoup
import urllib.request

url = 'https://www.gettyimages.in/photos/empty-roads' # Replace with the URL of the webpage you want to download images from
save_directory = 'images' # Replace with the directory where you want to save the images

if not os.path.exists(save_directory): # Check if the save_directory already exists
    os.makedirs(save_directory) # If it doesn't, create the directory

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
image_tags = soup.find_all('img') # Find all  tags in the HTML

for image_tag in image_tags:
    if image_tag.has_attr('src'): # Check if the tag has a 'src' attribute
        image_url = image_tag['src'] # Get the image url from the tag's 'src' attribute
        filename = image_url.split('/')[-1] # Extract the filename from the url
        filepath = os.path.join(save_directory, filename) # Create the filepath by combining the save_directory and filename
        try:
            urllib.request.urlretrieve(image_url, filepath) # Download the image and save it in the filepath
            print(f"{filename} saved in {save_directory}")
        except:
            print(f"Failed to save {filename} in {save_directory}") # If download fails, print error message.