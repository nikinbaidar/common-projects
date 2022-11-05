#!/usr/bin/env python

import skimage
import numpy

image = numpy.array([0, 0.5, 0.503, 1.])
print(image.dtype)

image = skimage.util.img_as_ubyte(image)
print(image.dtype)

image = skimage.util.img_as_float(image)
print(image.dtype)

