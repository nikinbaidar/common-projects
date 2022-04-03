#  _____________________________ 
# / Point Operations: Histogram \
# \ Equalization                /
#  ----------------------------- 
#         \   ^__^
#          \  (oo)\_______
#             (__)\       )\/\
#                 ||----w |
#                 ||     ||

import cv2
import numpy
from matplotlib import pyplot

def equalilzeHistogram(histogram, resolution):
  """ ## Applies CDF to a histogram and returns the equalized histogram.
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
     * resolution: resolution of the original image. """

  def computeCDF():
    # List the frequecny of those unique intensity values
    grey_level_frequency = numpy.array([ histogram[value] 
      for value in range(256) if histogram[value] ]).reshape(-1,1)

    unique_gray_level_count = numpy.shape(grey_level_frequency)[0]

    cdf = numpy.array([ numpy.sum(grey_level_frequency[0:index+1]) 
      for index in range(unique_gray_level_count) ]).reshape(-1,1)

    return cdf

  def normalizeCDF():
    """ Returns the equalized histogram. """
    hist_equalized = numpy.array(numpy.zeros(cdf.shape[0])).reshape(-1,1)
    scaling_factor = 256 - 1
    cdf_minimum    = numpy.min(cdf)
    denominator    = resolution - cdf_minimum

    for item in range(cdf.shape[0]):
      numerator = cdf[item] - cdf_minimum
      hist_equalized[item] = numerator / denominator * scaling_factor

    return numpy.round(hist_equalized)

  # List all unique pixel intensity values in the image
  existing_pixels = numpy.array([ value for value in range(256) 
     if histogram[value] ]).reshape(-1,1)

  # Acquire the CDF values
  cdf = computeCDF()
  histogram_equalized = normalizeCDF()
  table = numpy.hstack((existing_pixels, histogram_equalized))

  return table

def main():

  image = cv2.imread("./images/Lenna.png", 0)

  cv2.imshow("Original", image)
  cv2.waitKey()

  # image = numpy.array([[52, 55, 61,  59,  70,  61, 76, 61],
  #                      [62, 59, 55, 104,  94,  85, 59, 71],
  #                      [63, 65, 66, 113, 144, 104, 63, 72],
  #                      [64, 70, 70, 126, 154, 109, 71, 69],
  #                      [67, 73, 68, 106, 122,  88, 68, 68],
  #                      [68, 79, 60,  79,  77,  66, 58, 75],
  #                      [69, 85, 64,  58,  55,  61, 65, 83],
  #                      [70, 87, 69,  68,  65,  73, 78, 90]], 
  #                      dtype=numpy.uint8)

  rows        = image.shape[0]
  columns     = image.shape[1]
  resolution  = rows * columns

  # Compute the image histogram!
  image_histogram = cv2.calcHist([image], [0], None, [256], [0,255])

  table = equalilzeHistogram(image_histogram, resolution)

  print(table)

  # x = numpy.where(table==68)
  # print(x)

  # Replace Pixel values with the normalized CDF Values
  for i in range(rows):
    for j in range(columns):
      # Comput the row of the table that contains replacement for image[i,j]
      x = numpy.where(table==image[i][j])[0][0] 
      image[i,j] = table[x][1]

  image = numpy.array(image, dtype=numpy.uint8)
  print(image)
  cv2.imshow("Transformed", image)
  cv2.waitKey()
 
if __name__ == '__main__':
  main()
