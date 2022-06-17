#! /usr/bin/python
#  ______________________________________________________
# /\                                                     \
# \_| Filename    : edge_detection.py                    |
#   | Maintainer  : Nikin Baidar                         |
#   | Description : Edge detector functions              |
#   |   _________________________________________________|_
#    \_/___________________________________________________/

import cv2 as cv 
import numpy as np
import os

# Custom modules:
from convolution import addPadding, removePadding, pause
import spatial_filtering

def applyCanny(src, lower_bound, upper_bound, size=3):
    """ Canny edge detection. """

    def remapTheta(value):
        ''' Maps a given angle to one of 0, 45, 90 and 135.'''
        value = int(np.ceil(value)) % 180
        for boundary in ranges.keys():
            if (boundary[0] <= value) and (value < boundary[1]):
                mapping = ranges[boundary]
                return mapping

    src = src * 1.0
    m, n = src.shape[0], src.shape[1]
    strong_edge = upper_bound  

    ranges = {
                (0, 22.5)      : 0,
                (157.5, 181)   : 0,
                (22.5, 67.5)   : 45,
                (67.5, 112.5)  : 90,
                (112.5, 157.5) : 135,
            }

    # Apply gaussian filter of kernel size 3x3
    blurred = spatial_filtering.applyGaussinaSmoothing(src, size)

    # Calculate the intensity gradients and directions using sobel:
    edges_sobel = spatial_filtering.applySobel(blurred, size)
    gradient_x = edges_sobel.get('edges_x')
    gradient_y = edges_sobel.get('edges_y')
    gradient = np.sqrt(gradient_x**2 + gradient_y**2)
    theta = (np.arctan2(gradient_y, gradient_x)) * (180/np.pi)
    # print(theta)

    # Non maximum supression
    gradient = addPadding(gradient, borderType='replicate')

    for i in range(m):
        for j in range(n):
            if remapTheta(theta[i, j]) == 0:
                # Horizontal: east and west
                if (gradient[i,j] < gradient[i,j-1])   \
                or (gradient[i,j] < gradient[i,j+1]): 
                    gradient[i,j] = 0

            elif remapTheta(theta[i, j]) == 45:
                # Major diag: northeast and southwest
                if (gradient[i,j] < gradient[i-1,j+1]) \
                or (gradient[i,j] < gradient[i+1,j-1]): 
                    gradient[i,j] = 0

            elif remapTheta(theta[i, j]) == 90:
                # Vertical: north and south
                if (gradient[i,j] < gradient[i-1,j])   \
                or (gradient[i,j] < gradient[i+1,j]): 
                    gradient[i,j] = 0

            elif remapTheta(theta[i, j]) == 135:
                # Minor diag: Southeast and northwest
                if (gradient[i,j] > gradient[i-1,j-1]) \
                or (gradient[i,j] > gradient[i+1,j+1]): 
                    gradient[i,j] = 0
            else:
                print("error in remapping")

    # Double thresholding
    none_edge = np.where(gradient < lower_bound)
    sure_edge = np.where(gradient >= upper_bound)

    gradient[none_edge[0], none_edge[1]] = 0
    gradient[sure_edge[0], sure_edge[1]] = strong_edge

    # Edge tracking by hysteresis
    for i in range(m):
        for j in range(n):
            if gradient[i,j] >= lower_bound and gradient[i,j] < upper_bound:
                # Check for connection
                pixel_neighbourhood = gradient[i-1:i+2, j-1:j+2]
                if strong_edge in pixel_neighbourhood:
                    gradient[i,j] = strong_edge
                else:
                    gradient[i,j] = 0

    return removePadding(gradient)


def houghTransform(src):
    pass


def main():
    src = cv.imread('./images/Lenna.png', 0) 

    #########
    # Canny #
    #########

    edges_canny = applyCanny(src, 80, 100)
    edges_canny_cv = cv.Canny(src, 80, 100)

    cv.imshow("Edge detection using built in ", edges_canny_cv)
    cv.imshow("Edge detection using Canny edge algorithm", edges_canny)

    cv.imshow("Source", src)
    pause();

if __name__ == '__main__':
  main()
