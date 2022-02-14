#! /usr/bin/python

import cv2
import numpy

from os import system

system ("clear")

img = cv2.imread("./images/stock-photo.duckduckgo.com.jpg", 0)/255
noise = numpy.random.normal(0.2, 0.9, img.shape)
print(noise)
# cv2.imshow("My Index", noise)

# while True:
#     if cv2.waitKey() == 27:
#         cv2.destroyAllWindows()
#         break
