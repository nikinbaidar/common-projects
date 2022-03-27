#!/usr/bin/env python

"""
 ________________________ 
< Histogram Equalization >
 ------------------------ 
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"""

import cv2
import numpy
from matplotlib import pyplot

image = cv2.imread("./images/ultrasound-fetus.duckduckgo.com.jpg", 0)

image_histogram = cv2.calcHist(image, [0], None, [256], [0,256])

existing_pixels = []
frequency = []
pixel_count = 0

for gray_level in range(256) :
  gray_level_count = image_histogram[gray_level]
  if gray_level_count > 0:
    existing_pixels.append(gray_level)
    # Frequency of pixels with the current gray level
    frequency.append(gray_level_count)
    pixel_count = pixel_count + 1

existing_pixels = numpy.array(existing_pixels).reshape(-1,1)
frequency = numpy.array(frequency).reshape(-1,1)
N = numpy.sum(frequency)

# Calculate cumulative distribution value
cdf = numpy.array(numpy.zeros(pixel_count)).reshape(-1,1)

for i in range(pixel_count):
  for j in range(i+1):
    cdf[i] = cdf[i] + frequency[j] 
  cdf[i] = cdf[i]/N

table = numpy.hstack((existing_pixels, frequency))
print(table)

# Equalize the histogram by applying the CDF
hist_equalized = numpy.array(numpy.zeros(pixel_count)).reshape(-1,1)

cdf_minimum = min(cdf)
resolution  = image.shape[0] * image.shape[1]
denominator = cdf_minimum * resolution

number_of_gray_levels = 256

for i in range(pixel_count):
  numerator = cdf[i] - cdf_minimum
  hist_equalized[i] = numerator/denominator * (number_of_gray_levels - 1)
 
pyplot.plot(image_histogram, label="Original Histogram")
pyplot.xlabel("Intensities")
pyplot.ylabel("Count")
pyplot.title("Histogram: Pixel Intensities v/s Pixel Counts")
pyplot.legend()
pyplot.grid(linewidth=0.5)
pyplot.show()

# pyplot.plot(existing_pixels, hist_equalized, 
#     color='r', label="Equalized Histogram")
# pyplot.xlabel("Intensities")
# pyplot.ylabel("Cumulative Fraction of Pixel Counts")
# pyplot.title("Histogram: Pixel Intensities v/s Cumulative Fraction of pixels")
# pyplot.legend()
# pyplot.grid(linewidth=0.5)
# pyplot.show()

