#! /usr/share/python

'''
Speckle noise is multiplicitive noise, having a granular pattern.
Inherent in ultrasound images.
The small part of the returning sound pulse gets mirrored back into the tissues
by the transducer surface itself, and generates a new echo. The backscattered
echoes give rise to speckle noise.

Reference for spekcle modelling: https://bit.ly/3umKfZS
'''

# Import necessary modules
import cv2
import numpy
from os import system
from matplotlib import pyplot

def addSpeckleNoise(image, scale):
    noise = numpy.random.rayleigh(scale, image.shape)
    noisy_image = image * noise
    return noise

def addSpeckleNoise2(image, MEAN, VARIANCE):
    noise = numpy.random.normal(MEAN, VARIANCE, image.shape)
    noisy_image = image * (1 + noise)
    return noise

system("clear")

image = cv2.imread("./images/satellite-image.png", \
        cv2.IMREAD_GRAYSCALE)/255.0

speckle_noisy_img = addSpeckleNoise(image, 0.2)
speckle_noisy_img2 = addSpeckleNoise2(image, 0.2, 0.9)

# Display images
cv2.imshow("Speckle Noisy Image", speckle_noisy_img)
cv2.imshow("Speckle Noisy Image using Gaussina Noise", speckle_noisy_img2)
cv2.imshow("Original Image", image)

# Close only when escape is pressed
while True:
    if cv2.waitKey() == 27:
        cv2.destroyAllWindows()
        break

# Histogram plots
# pyplot.hist(image.ravel(), bins = 256)
# pyplot.show()

# pyplot.hist(speckle_noisy_img2.ravel(), bins = 256)
# pyplot.show()

# pyplot.hist(speckle_noisy_img.ravel(), bins = 256)
# pyplot.show()
