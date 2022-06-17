# !/usr/bin/env python
#  /"\/\_..---------------------------------------------._/\/"\
# (     _|| Filename    : entropy.py                   ||_     )
#  \_/\/ || Maintainer  : Nikin Baidar                 || \/\_/
#        || Description : Calculate entropy of images. ||
#  /"\/\_|----------------------------------------------|_/\/"\
# (     _|                                              |_     )
#  \_/\/ `----------------------------------------------' \/\_/

import cv2 as cv
import numpy as np
import skimage.measure


def getHist(image):
    return np.array([len(np.nonzero(image == pixel)[0])
        for pixel in range(256)]).reshape(256, 1)


def getEntropy(image):
    img_hist = getHist(image)
    resolution = image.size
    probability = np.array([ (img_hist[i]/resolution)[0]
        for i in range(256) if img_hist[i] ])
    return (-1) * np.sum(probability * np.log2(probability))


def main():
    img = cv.imread('./images/Lenna.png')

    print(f'Entropy calculated by custom function = {getEntropy(img)}')

    print('Entropy calculated by built-in function = ' \
            f'{skimage.measure.shannon_entropy(img)}')


if __name__ == '__main__':
    main()
