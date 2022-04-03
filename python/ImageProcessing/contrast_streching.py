#  ______________________________________ 
# < Point Operation: Contrast Stretching >
#  -------------------------------------- 
#        \   ^__^
#         \  (oo)\_______
#            (__)\       )\/\
#                ||----w |
#                ||     ||


import numpy
import cv2
from matplotlib import pyplot

def plotHistogram(image_histogram, processed_image_histogram, plotTitle=""):
  pyplot.plot(image_histogram.ravel(), label="Original")
  pyplot.plot(processed_image_histogram.ravel(), label="Processed")
  pyplot.xlabel("Pixel Intensities")
  pyplot.ylabel("Frequency")
  pyplot.title(plotTitle)
  pyplot.legend()
  pyplot.show()

def stretchContrast(image):
  # Comput Histogram
  image_histogram = cv2.calcHist([image], [0], None, [256], [0, 255])
  existing_pixels = numpy.array([ value for value in range(256) 
    if image_histogram[value] ])

  a = 0
  b = 255
  c = numpy.min(existing_pixels)
  d = numpy.max(existing_pixels)

  scaling_factor = (b - a)/(d - c)

  transformed_image = ((image - c) * scaling_factor) + a

  return transformed_image

image = cv2.imread('./images/Lenna.png')

image_histogram = cv2.calcHist([image], [0], None, [256], [0, 255])

contrast_streched_image = stretchContrast(image)
contrast_streched_image = numpy.array(contrast_streched_image,
    dtype=numpy.uint8)

histogram_streched = cv2.calcHist([contrast_streched_image], [0], None, [256],
    [0,255])

# histogram plots
plotHistogram(image_histogram, histogram_streched, 
    plotTitle="Original v/s Contrast Stretched")
