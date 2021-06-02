""" setting up initial variables """

import os
import numpy as np
import PIL
import cv2

# getting the number of files in the directory that you choose, can also just manually change this value if you
# already know it but for computation in the rest of the program its useful to keep the DIR of all the images
DIR = '/Volumes/GoogleDrive/My Drive/CS Projects/GradientMaker/Edits'
total_images = (len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

# set the dimensions of the final product you want
final_width = 21
final_height = 10

# to open the base gradient image and read its values as RGB
image = cv2.imread("/Volumes/GoogleDrive/My Drive/CS Projects/GradientMaker/Base.jpg") # base is 480x270
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
height = image.shape[0] # 270
width = image.shape[1] # 480
height_increment = int(height / final_height)
width_increment = int(width / final_width)
colour_goals = [[0 for x in range(final_width)] for y in range(final_height)]
x = 0
y = 0
print(height_increment, width_increment)
for i in range(final_height):
    x = height_increment * i
    for j in range(final_width):
        y = width_increment * j
        # print("i = {}, j = {}".format(i,j))
        # print("x = {}, y = {}".format(x,y))
        colour_goals[i][j] = image[x, y]
print(colour_goals[5][7])




# list of all the filenames in the given directory
image_names = os.listdir(DIR)

for name in image_names:
    print(DIR + '/' + name)
    image = cv2.imread(DIR + '/' + name)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # reshape the image to a 2D array of pixels and 3 color values (RGB)
    pixel_values = image.reshape((-1, 3))
    # convert to float
    pixel_values = np.float32(pixel_values)

    # define stopping criteria so that my computer doesnt explode
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)

    # number of clusters (K)
    k = 3

    # labels tells us which cluster we are looking at
    # we randomly assign the first set of clusters to ensure full accuracy
    _, labels, (centers) = cv2.kmeans(pixel_values, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # convert back to 8 bit values
    centers = np.uint8(centers)

    # flatten the labels array
    labels = labels.flatten()

    # convert all pixels to the color of the centroids
    segmented_image = centers[labels.flatten()]


    print(segmented_image[0])