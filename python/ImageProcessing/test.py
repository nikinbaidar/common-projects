#! /usr/bin/python

import cv2
import numpy

image = numpy.array([[0, 2, 3], [4,5,6], [7,8,9]])

print(0 in image)

image = numpy.array([[1, 2, 3], [4,5,6], [7,8,9]])

print(0 in image)
