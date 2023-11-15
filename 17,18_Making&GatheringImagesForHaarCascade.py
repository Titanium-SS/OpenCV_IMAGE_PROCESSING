"""
Simple script for Web Scraping images for a new haar Cascade Training
"""

import urllib.request
import cv2
import os


def store_raw_images():
    neg_images_link = 'https://www.bing.com/images/search?q=Empty+roads&form=HDRSC3&first=1'  # Link 1 for negatives

    # https://source.unsplash.com/random/?empty-roads   -->  Check at home

    neg_image_urls = urllib.request.urlopen(neg_images_link).read().decode()

    if not os.path.exists('neg'):
        os.makedirs('neg')

    """
    When URL 1 is done, run the second url while 
    upgrading this variable to the no. 1 greater than
    the no. represented by the last pic in the directory
    """

    pic_num = 1

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "neg/" + str(pic_num) + '.jpg')
            img = cv2.imread("neg/" + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("neg/" + str(pic_num) + '.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


store_raw_images()
