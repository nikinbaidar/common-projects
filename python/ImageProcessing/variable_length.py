#!/usr/bin/env python
import cv2 as cv
import numpy as np
import skimage.measure    


def getEntropy(image):
    image_hist = cv.calcHist([image], [0], None, [256], [0, 255])
    resolution = image.shape[0] * image.shape[1]
    possibleGrayLevelCount = len(image_hist)
    probability = [(image_hist[i]/resolution)[0] 
            for i in range(possibleGrayLevelCount)]

    probability_existing_pixels = list(filter(
        lambda probability: probability > 0, probability))

    entropy = (-1) * np.sum(np.multiply(probability_existing_pixels,
        np.log2(probability_existing_pixels)))
    return image_hist, entropy

image = cv.imread('./images/Lenna.png', 0);

image_hist, entropy = getEntropy(image)

existing_pixels = np.array([i for i in range(len(image_hist))
    if image_hist[i] > 0])

pixel_frequencies = np.array([int(image_hist[i][0])
    for i in range(len(image_hist)) if image_hist[i] > 0])

# print(existing_pixels, pixel_frequencies, sep='\n'*2)
# print()

mapping = {existing_pixels[i]: pixel_frequencies[i] for i in range(len(existing_pixels))}
mapping_sorted = sorted(mapping.items(), key=lambda x:x[1])

nodes = mapping_sorted

print(mapping_sorted)
# pixel_frequencies_sorted = np.sort(pixel_frequencies)


# Create a dictonary


# print(pixel_frequencies_sorted)

