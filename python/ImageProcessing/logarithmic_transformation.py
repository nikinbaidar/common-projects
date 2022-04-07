#  ______________________________________________________________
# /\                                                             \
# \_| Filename    : logarithmic_transformation.py                |
#   | Maintainer  : Nikin Baidar                                 |
#   | Description : Point Operation (Logarithmic Transformation) |
#   |   _________________________________________________________|_
#    \_/___________________________________________________________/
# 

import cv2
import numpy
from matplotlib import pyplot

def plotHistogram(input_image, processed_image, plotTitle="", bins=256):
  pyplot.hist(input_image.ravel(), label="Original", bins=bins)
  pyplot.hist(processed_image.ravel(), label="Processed", bins=bins)
  pyplot.xlabel("Pixel Intensities")
  pyplot.ylabel("Frequency")
  pyplot.title(plotTitle)
  pyplot.legend()
  pyplot.show()


def logarithmically_transform(image, output_datatype=numpy.uint8):
  """ ## Returns logarithmically transformed image.
  ## Logarithmic transformation:
     $$
     c = 255 / log(1 + max_input_pixel_intensity)
     s = c * log(1+r)
     $$
     where,
       - s is the output/processed pixel.
       - c is the scaling factor
       - r is the input pixel
  ## Parameters:
     * image: The input image which is to be transformed.
     * output_datatype (default numpy.uint8): The return type for the output. 
       The ouput datatype should match the input datatype. """

  max_input_pixel_intensity = numpy.max(image)
  scaling_factor = 255 / (numpy.log(1 + max_input_pixel_intensity))
  ones = numpy.ones(image.shape)
  transformed_image = scaling_factor * numpy.log(image + ones)
  transformed_image = numpy.array(transformed_image, dtype=output_datatype)

  return transformed_image


def main():
  input_image = cv2.imread("./images/Lenna.png")
  processed_image = logarithmically_transform(input_image)

  # Display processed image
  cv2.imshow("Logarithmically Processed Image", processed_image)
  cv2.waitKey()
  cv2.destroyAllWindows()

  # Histogram plots
  plotHistogram(input_image, processed_image, plotTitle="Image Histogram: "\
      "Lenna Original and Logarithmic Transformation")

if __name__ == '__main__':
  main()
