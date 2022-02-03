#! /usr/bin/python

import cv2 as cv
import numpy as np
import matplotlib
matplotlib.use('TkAgg')

from os import system
from matplotlib import pyplot as plt
from copy import deepcopy
from time import sleep

system ("clear")

# Reading Images

img = cv.imread("/home/nikin/Pictures/random_illustrations/japan.jpg")

row,col,depth = img.shape # [length, bredth, depth]
y = np.zeros(256, np.uint16)
print(y.shape)

print(img[0,0]) # 170 158 148
y[[170,158,148]] += 1

print(y[170], y[158], y[148])
print(y[[170,158,148]])

# x = np.arange(0,256)
# plt.bar(x,y,color="gray", align = "center")
# plt.show()



# # Displaying Images
# cv.imshow("Original", img)

# Close on escape
while True:
    if cv.waitKey(0) & 0xFF == 27:
        cv.destroyAllWindows()
        break
