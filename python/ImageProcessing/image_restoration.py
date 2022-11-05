# !/usr/bin/env python
#
#  /"\/\_..---------------------------------------------------._/\/"\
# (     _|| Filename    : image_restroation.py               ||_     )
#  \_/\/ || Maitaner    : Nikin Baidar                       || \/\_/
#        || Description : Reduce noise and restore an image. ||
#        ||               Using deconvolution.               ||
#  /"\/\_|----------------------------------------------------|_/\/"\
# (     _|                                                    |_     )
#  \_/\/ `----------------------------------------------------' \/\_/

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

from create_noise import addGaussianNoise
import convolution as conv
import dft2D as dft

def padding(image, wanted_depth):
    x, y = image.shape[0],  image.shape[1]
    h, v = wanted_depth[0], wanted_depth[1]

    a = (h - x) // 2
    b = (v - y) // 2

    depth_x = (a, h - a - x)
    depth_y = (b, v -b - y)

    return np.pad(image, pad_width=(depth_x, depth_y))


def getGaussianFilter(size, sigma=1.0):
    """ Get a filter of size and sigma. """
    size = size // 2
    x, y = np.mgrid[-size:size+1, -size:size+1]
    filter = (1 / (2 * np.pi * sigma**2)) * (np.exp(-(x**2 + y**2)/2))
    filter = filter / (np.sum(filter) if np.sum(filter) != 0 else 1)
    return filter


def main():
    src = cv.imread('./images/stock-photo.duckduckgo.com.jpg',
          cv.IMREAD_GRAYSCALE) / 255.0

    src = addGaussianNoise(src, MEAN=0.1, VARIANCE=0.3)

    # src_padded = conv.addPadding(src, borderType='zero', depth=1)

    srcFrequencyDomain = dft.spatial2frequency(src, shift=True)
    srcFrequencyImage = srcFrequencyDomain.get('magnitude')
    srcFrequencyImage_visulization = np.log(srcFrequencyImage
            + np.ones_like(srcFrequencyImage))

    # Genarate a PSF
    gf = getGaussianFilter(21,21)
    gf = padding(gf, wanted_depth=srcFrequencyImage.shape)

    psfFrequencyDomain = dft.spatial2frequency(gf, shift=True)
    psfFrequencyImage = psfFrequencyDomain.get('magnitude')
    psfFrequencyImage_visulization = np.log(psfFrequencyImage
            + np.ones_like(psfFrequencyImage))


    restoredFrequencyImage = np.divide(srcFrequencyImage , psfFrequencyImage)
    restoredFrequencyImage_visulization = np.log(psfFrequencyImage
            + np.ones_like(psfFrequencyImage))

    restoredSpatialDomain = np.abs(np.fft.ifft2(restoredFrequencyImage))
    restoredSpatialDomain = np.array(restoredSpatialDomain, dtype=np.uint8)


    # Outputs
    # plt.imshow(srcFrequencyImage_visulization, cmap='gray')
    # plt.title("Source padded F domain")
    # plt.show()

    # plt.imshow(psfFrequencyImage_visulization, cmap='gray')
    # plt.title("PSF F domain")
    # plt.show()

    # plt.imshow(restoredFrequencyImage_visulization, cmap='gray')
    # plt.title("Restored F domain")
    # plt.show()

    cv.imshow('Restored image', restoredSpatialDomain)
    cv.imshow('Source image', src)
    conv.pause()


if __name__ == '__main__':
    main()
