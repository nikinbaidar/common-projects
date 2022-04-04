#!/usr/bin/env python
#  __________________________________________________________
# /\                                                         \
# \_| Filename    : histogram_equalization.py                |
#   | Maintainer  : Nikin Baidar                             |
#   | Description : Point Operation (Histogram Equlaization) |
#   |   _____________________________________________________|_
#    \_/_______________________________________________________/


from matplotlib import pyplot

import cv2
import numpy


def equalilzeHistogram(histogram, resolution):
  """ ## Applies CDF to a histogram and returns the equalized histogram. The 
  size of the equlaized histogram may not be same as the original depending on
  how many unique pixels exists in the image.
  ### (CDF) Cumulative Distribution function:
      $$
      CDF(i) = \sum_{j<=i} h(j)

      H(v) =  CDF(v) - CDF_{min}
             -------------------- x (L - 1)
             (M x N) - CDF_{min}
      $$
      where, 
        - L is the highest possible pixel intensity.
  ## Parameters:
     * histogram: The input histogram that is to be equlaized
     * resolution: resolution of the original image.
  ## Return Type: <class : 'list'>. """

  def computeCDF(histogram):
    # List the frequecies of all unique intensity values
    # Image histogram but only existing grey levels are listed
    unique_grey_level_frequencies = numpy.array([histogram[value] 
      for value in range(256) if histogram[value]])
    unique_gray_level_count = unique_grey_level_frequencies.shape[0]

    cdf = numpy.array([numpy.sum(unique_grey_level_frequencies[0:index+1]) 
      for index in range(unique_gray_level_count)])

    return cdf

  # Acquire the CDF values
  cdf = computeCDF(histogram)

  hist_equalized = numpy.array(numpy.zeros(cdf.shape[0])).reshape(-1,1)

  # Apply the transformation function
  scaling_factor = 256 - 1
  cdf_minimum    = numpy.min(cdf)
  denominator    = resolution - cdf_minimum

  for item in range(cdf.shape[0]):
    numerator = cdf[item] - cdf_minimum
    hist_equalized[item] = numerator / denominator * scaling_factor

  hist_equalized =  numpy.round(hist_equalized)

  return list(hist_equalized)


def transformHistogram(image):

  rows        = image.shape[0]
  columns     = image.shape[1]
  resolution  = rows * columns

  image_histogram = cv2.calcHist([image], [0], None, [256], [0,255])
  hist_equalized  = equalilzeHistogram(image_histogram, resolution)

  # List all unique pixel intensity values in the image
  existing_pixels = [value for value in range(256) if image_histogram[value]]

  # Replace existing pixels with the new (equalized) histogram values
  for i in range(rows):
    for j in range(columns):
      index       = existing_pixels.index(image[i,j])
      replacement = hist_equalized[index]
      image[i,j]  = replacement

  image = numpy.array(image, dtype=numpy.uint8)

  return image


def main():

  # image = cv2.imread("./images/Lenna.png", 0)

  # # Display the input image
  # cv2.imshow("Original", image)
  # cv2.waitKey()

  image = numpy.array([[52, 55, 61,  59,  70,  61, 76, 61],
                       [62, 59, 55, 104,  94,  85, 59, 71],
                       [63, 65, 66, 113, 144, 104, 63, 72],
                       [64, 70, 70, 126, 154, 109, 71, 69],
                       [67, 73, 68, 106, 122,  88, 68, 68],
                       [68, 79, 60,  79,  77,  66, 58, 75],
                       [69, 85, 64,  58,  55,  61, 65, 83],
                       [70, 87, 69,  68,  65,  73, 78, 90]], 
                       dtype=numpy.uint8)
  
  print(image)

  transfomred_image = transformHistogram(image)

  print()
  print(transfomred_image)

  # # Display Transformed Image
  # cv2.imshow("Transformed", transfomred_image)
  # cv2.waitKey()
 
if __name__ == '__main__':
  main()
