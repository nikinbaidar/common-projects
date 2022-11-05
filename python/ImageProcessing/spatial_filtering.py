#! /usr/bin/python
#  ______________________________________________________
# /\                                                     \
# \_| Filename    : saptial_filtering.py                 |
#   | Maintainer  : Nikin Baidar                         |
#   | Description : Spatial filtering operations         |
#   |   _________________________________________________|_
#    \_/___________________________________________________/

import cv2 as cv 
import numpy as np
import os

from convolution import addPadding, removePadding, pause


def applyLaplacianFilter(src):
    l = np.array([
        [0.0, -1.0, 0.0, ], 
        [-1.0, 4.0, -1.0, ], 
        [0.0, -1.0, 0.0, ]])
    print(l)
    output = cv.filter2D(src, -1, l)
    return output


def applyPrewitt(src, size):
    k = size // 2
    x,y = np.mgrid[(-1*k):k+1, (-1*k):(k+1)]
    print(x,y, sep='\n'*2)
    gradient_x = cv.filter2D(src, -1, x) 
    gradient_y = cv.filter2D(src, -1, y) 
    gradient_xy = gradient_x + gradient_y
    return {
            'edges_x'  : gradient_x,
            'edges_y'  : gradient_y,
            'edges_xy' : gradient_xy
            }


def applySobel(src, size) :
    k = size // 2
    x,y = np.mgrid[(-1*k):k+1, (-1*k):(k+1)]
    x[k,:] *= 2
    y[:,k] *= 2
    # print(x,y, sep='\n'*2)
    gradient_x = cv.filter2D(src, -1, x) 
    gradient_y = cv.filter2D(src, -1, y) 
    gradient_xy = gradient_x + gradient_y
    return {
            'edges_x'  : gradient_x,
            'edges_y'  : gradient_y,
            'edges_xy' : gradient_xy
            }


def applyBoxBlurring(src, size, strength=1):
    filter = np.ones((size, size))
    filter /= np.sum(filter)
    for i in range(strength):
        blurred = cv.filter2D(src, -1, filter) 
        src = blurred
    return blurred


def applyGaussinaSmoothing(src, size, strength=1):

    def getGaussianFilterUsingLoop(size):
        sigma = 1.0
        n = int(size) // 2
        normalizer = 1 / (2 * np.pi * sigma**2)
        filter = np.zeros((size,size))
        for i in range(-n, n+1):
            for j in range(-n, n+1):
                num = (i)**2 + (j)**2 
                den = 2* sigma**2
                filter[i+n, j+n] = np.exp(-(num/den)) * normalizer
        return filter

    def getGaussianFilter(size, sigma=1.0):
        """ Get a filter of size and sigma. """
        size = size // 2
        x, y = np.mgrid[-size:size+1, -size:size+1]
        filter = (1 / (2 * np.pi * sigma**2)) * (np.exp(-(x**2 + y**2)/2))
        filter = filter / (np.sum(filter) if np.sum(filter) != 0 else 1)
        return filter

    filter = getGaussianFilter(size)
    for i in range(strength):
        blurred = cv.filter2D(src, -1, filter) 
        src = blurred
    return blurred


def main():
    src = cv.imread('./images/Lenna.png', 0) 

    #####################
    # Gaussian blurring #
    #####################

    # g_blurred_image_1 = applyGaussinaSmoothing(src, 3)
    # g_blurred_image_9 = applyGaussinaSmoothing(src, 3, 9)
    # cv.imshow("Gaussian blur output strength: 1", g_blurred_image_1)
    # cv.imshow("Gaussian blur output strength: 9", g_blurred_image_9)

    ################
    # Box blurring #
    ################

    # box_blurred_image_1 = applyBoxBlurring(src, 3, 1)
    # box_blurred_image_9 = applyBoxBlurring(src, 3, 9)
    # cv.imshow("Box blur output strength: 1", box_blurred_image_1)
    # cv.imshow("Box blur output strength: 9", box_blurred_image_9)

    ####################
    # Prewitt Operator #
    ####################

    # edges_prewitt = applyPrewitt(src, 3)
    # edges_prewitt_x = edges_prewitt.get('edges_x')
    # edges_prewitt_y = edges_prewitt.get('edges_y')
    # edges_prewitt_xy = edges_prewitt.get('edges_xy')
    
    # cv.imshow("Horizontal Edge detection using prewitt", edges_prewitt_x)
    # cv.imshow("Vertical Edge detection using prewitt", edges_prewitt_y)
    # cv.imshow("Both Edge detection using prewitt", edges_prewitt_xy)

    ##################
    # Sobel Operator #
    ##################

    # edges_sobel = applySobel(src, 3)
    # edges_sobel_x = edges_sobel.get('edges_x')
    # edges_sobel_y = edges_sobel.get('edges_y')
    # edges_sobel_xy = edges_sobel.get('edges_xy')
    
    # cv.imshow("Horizontal Edge detection using Sobel", edges_sobel_x)
    # cv.imshow("Vertical Edge detection using Sobel", edges_sobel_y)
    # cv.imshow("Both Edge detection using Sobel", edges_sobel_xy)

    ####################
    # Laplacian filter #
    ####################

    # edges_laplacian = applyLaplacianFilter(src)
    # cv.imshow("Edge detection using Laplacian filter", edges_laplacian)

    cv.imshow("Source", src)
    pause();

if __name__ == '__main__':
  main()
