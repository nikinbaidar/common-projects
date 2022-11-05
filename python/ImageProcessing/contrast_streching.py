#! /usr/bin/env python
#  _____________________________________________________
# | Filename    : contrast_streching.py                 |
# | Author      : Nikin Baidar                          |
# | Description : Point Operation (Contrast Stretching) |
# |________________________________________________  __'\
#                                                  |/   \\
#                                                   \    \\  .
#                                                        |\\/|
#                                                        / " '\
#                                                        . .   .
#                                                       /    ) |
#                                                      '  _.'  |
#                                                      '-'/    \

from matplotlib import pyplot

import numpy
import cv2


def plotHistogram(image_histogram, processed_image_histogram, plotTitle=""):
  pyplot.plot(image_histogram.ravel(), label="Original")
  pyplot.plot(processed_image_histogram.ravel(), label="Processed")
  pyplot.xlabel("Pixel Intensities")
  pyplot.ylabel("Frequency")
  pyplot.title(plotTitle)
  pyplot.grid(linewidth=0.2)
  pyplot.legend()
  pyplot.show()


def strechContrast(image, hist):
  """ ## Returns a contrast stretched image.
  ## Contrast Stretching
     $$
     s = (r-c) (b-a)/(d-c) + a
     $$
     where, 
      - s is the processed pixel
      - r is the input pixel
      - c is the lowest pixel that exists in the image
      - d is the highest pixel that exists in the image
      - a and b is the range of the possible pixel values
  ## Parameters:
     * image: The image whose contrast is to be streched.
     * histogram: The histogram of the original image. """

  # List all intensity value that exists in the image.
  existing_pixels = [ value for value in range(256) if hist[value] ]

  a = 0
  b = 255
  c = min(existing_pixels)
  d = max(existing_pixels)

  # Compute the scaling factor
  scaling_factor = (b - a)/(d - c)

  # Apply tranformation function
  transformed_image = ((image - c) * scaling_factor) + a
  return transformed_image


def main():
  image = cv2.imread('./images/Lenna.png')
  image_histogram = cv2.calcHist([image], [0], None, [256], [0, 255])

  contrast_streched_image = strechContrast(image, image_histogram)
  contrast_streched_image = numpy.array(contrast_streched_image,
      dtype=numpy.uint8)
  histogram_streched = cv2.calcHist([contrast_streched_image], [0],
      None, [256], [0,255])

  plotHistogram(image_histogram, histogram_streched, 
      plotTitle="Original v/s Contrast Stretched")


if __name__ == '__main__':
  main()
