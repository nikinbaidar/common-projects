#! /usr/bin/python
#  ______________________________________________________
# /\                                                     \
# \_| Filename    : 2Ddft.py                             |
#   | Maintainer  : Nikin Baidar                         |
#   | Description : Image Transformation                 |
#   |               (2D Discrete Fourier Transfomration) |
#   |   _________________________________________________|_
#    \_/___________________________________________________/

import numpy
import cv2
from matplotlib import pyplot

def DFT(image, u, v):
  M, N = image.shape[0], image.shape[1]
  sum = 0
  for x in range(M):
    for y in range(N):
      sum += image[x,y] * numpy.exp(-2j * numpy.pi * 
          ((u * x)/M + (v * y)/N))  
  sum /= (M*N)
  return (round(sum.real, 2) + round(sum.imag, 2) * 1j)


def main():

  # image = numpy.array([[0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0],
  #                      [0, 1, 1, 0, 0, 1, 1, 0]],
  #                      dtype=numpy.uint8)

  image = cv2.imread('./images/ultrasound-fetus.duckduckgo.com.jpg', 0)

  rows = image.shape[0]
  cols = image.shape[1]


  out_fft = numpy.fft.fft2(image)
  # for u in range(rows):
  #   for v in range(cols):
  #     print("I({},{}) = {}".format(u,v ,out_fft[u][v]))
  
  frequency_domain = numpy.log(numpy.abs(out_fft))

  pyplot.imshow(frequency_domain, 'gray')
  pyplot.show()

  # for u in range(rows):
  #   for v in range(cols):
  #     dft_image = DFT(image, u=u, v=v)
  #     print("I({},{}) = {}".format(u,v ,dft_image))


if __name__ == '__main__':
  main()
