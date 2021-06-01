""" setting up initial variables """

import os
import numpy as np
import PIL
import cv2

# getting the number of files in the directory that you choose, can also just manually change this value if you already know it
# but for computation in the rest of the program its useful to keep the DIR of all the images
DIR = '/Volumes/GoogleDrive/My Drive/CS Projects/GradientMaker/Edits'
total_images = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# set the dimensions of the final product you want
length = 21
height = 10

# list of all the filenames in the given directory
image_names = os.listdir(DIR)

for name in image_names:
    image = cv2.imread(DIR + '/' + name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixel_values = image.reshape((-1, 3))
    # convert to float
    pixel_values = np.float32(pixel_values)
