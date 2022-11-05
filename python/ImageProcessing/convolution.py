# !/usr/bin/env python
#  ______________________________________________________________________
# /\                                                                     \
# \_| Filename    : convolution.py                                       |
#   | Maintaner   : Nikin Baidar                                         |
#   | Description : Convolution and correlation with and without padding |
#   |   _________________________________________________________________|_
#    \_/___________________________________________________________________/

import os
import numpy as np
from copy import deepcopy

import cv2 as cv
from skimage.util import img_as_ubyte
import statistics

################################################
# cv2 borders:                                 #
#     cv2.BORDER_CONSTANT (16) -> Zero padding #
#     cv2.BORDER_REFLECT_REPLICATE             #
#     cv2.BORDER_REFLECT                       #
#     cv2.BORDER_WRAP                          #
################################################


def pause():
    """ After displaying an image wait until Escape (ASCII 27) 
    is pressed. 
    """
    while cv.waitKey() != 27:
        continue
    cv.destroyAllWindows()
    return 0


def addPadding(image, borderType='zero|replicate', depth=1):
    """ Adding padding to images.
    * Args:
        image
        borderType = (str) zero or replicate
        depth = (int) padding depth
    """
    # h_pad -> x = add columns 
    # v_pad -> y = add rows

    def replicateBorder(image):
        h_pad_left = image[:,0].reshape(-1,1)
        h_pad_right = image[:,-1].reshape(-1,1)
        v_pad_up = np.hstack(([0], image[0,:], [0]))
        v_pad_down = np.hstack(([0], image[-1,:], [0]))
        image = np.hstack((h_pad_left, image, h_pad_right))
        image = np.vstack((v_pad_up, image, v_pad_down))
        return image

    def zeroPadding(image):
        x, y = image.shape[0], image.shape[1]
        h_pad = np.zeros(x).reshape(-1,1)
        image = np.hstack((h_pad, image, h_pad))
        v_pad = np.zeros(y+2) 
        image = np.vstack((v_pad, image, v_pad))
        return image

    for i in range(depth):
        if borderType == 'zero':
            image = zeroPadding(image)
        elif borderType == 'replicate':
            image = replicateBorder(image)

    return image


def removePadding(paddedImage, depth=1):
    for i in range(depth):
        x, y = paddedImage.shape[0] - depth, paddedImage.shape[1] - depth
        paddedImage = paddedImage[1:x,1:y]
    return paddedImage


def convolve(image, filter, mode=0, addBorder=False, borderType='zero'):
    if mode:
        # Flip the filter for convolution
        filter = (filter[-1::-1, -1::-1])

    if addBorder:
        image = addPadding(image, borderType=borderType)
        removeBorder = True
    else:
        removeBorder = False

    k = filter.shape[0]
    filter_size = k // 2
    # Make a copy of the original image.
    result_img = deepcopy(image)

    m,n = image.shape[0], image.shape[1]
    for x in range(m):
        for y in range(n):
            if x+k > m or y+k > n:
                continue
            pixels = image[x:x+k, y:y+k]
            product = pixels * filter 
            replacement = round(np.sum(product), 2)
            result_img[x+filter_size , y+filter_size] = replacement
            # print(product, replacement, pixels,  image, sep='\n'*2, end='\n'*2)
            # input()
            # os.system("clear")
    if removeBorder:
        result_img = removePadding(result_img)

    return result_img

def medianFilter(image, k, addBorder=False):
    if addBorder:
        image = addPadding(image)
        removeBorder = True
    else:
        removeBorder = False

    filter_size = k // 2
    result_img = deepcopy(image)
    m,n = image.shape[0], image.shape[1]
    result = np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if x+k > m or y+k > n:
                continue
            pixels = (image[x:x+k, y:y+k]).flatten()
            replacement = statistics.median(pixels)
            result_img[x+filter_size , y+filter_size] = replacement
    if removeBorder:
        result_img = removePadding(result_img)

    return img_as_ubyte(result_img/255.0)

def minFilter(image, k, addBorder=False):
    if addBorder:
        image = addPadding(image)
        removeBorder = True
    else:
        removeBorder = False

    filter_size = k // 2
    result_img = deepcopy(image)
    m,n = image.shape[0], image.shape[1]
    result_img = np.zeros((m,n))
    for x in range(m):
        for y in range(n):
            if x+k > m or y+k > n:
                continue
            pixels = (image[x:x+k, y:y+k]).flatten()
            replacement = np.min(pixels)
            result_img[x+filter_size , y+filter_size] = replacement
    if removeBorder:
        result_img = removePadding(result_img)

    return img_as_ubyte(result_img/255.0)

def main():
    src = np.array([
        [0, 0, 0, 0, 2, 0, 0, 0],
        [0, 1, 1, 1, 1, 0, 0, 1],    
        [0, 1, 1, 1, 1, 0, 0, 1],   
        [1, 1, 1, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1, 1, 1], 
        [0, 1, 1, 0, 0, 0, 1, 1], 
        [0, 1, 1, 0, 0, 0, 1, 1], 
        [0, 0, 0, 0, 7, 0, 0, 9]
        ], dtype=np.uint8)

    src = src * 1.0

    filter = np.array([
        [-1, 0, -1],
        [2, 0, -2],
        [-1, 0, -1,]])

    ###############
    # Convolution #
    ###############

    # print("Without padding:")
    # output = convolve(src,filter)
    # print(output)

    # print()
    # print("With border replicated:")
    # output = convolve(src, filter, addBorder=True, borderType='replicate')
    # print(output)

    # print()
    # print("open cv filter2D border replicated:")
    # print(cv.filter2D(src, -1, filter, borderType=cv.BORDER_REFLECT))

    # print()
    # print("With zero padding:")
    # output = convolve(src, filter, addBorder=True, borderType='zero')
    # print(output)

    # print()
    # print("open cv filter2D with zero padding:")
    # print(cv.filter2D(src, -1, filter, borderType=cv.BORDER_CONSTANT))

    ###################
    # Median Blurring #
    ###################

    # print("Without zero padding:")
    # output = medianFilter(src, 3, addBorder=False)
    # print(output)

    # print()
    # print("With zero padding:")
    # output = medianFilter(src, 3, addBorder=True)
    # print(output)

    # print()
    # print("open cv medianBlur with")
    # print(cv.medianBlur(img_as_ubyte(src/255), 3))

    #####################
    # Minimum Filtering #
    #####################

    


if __name__ == "__main__":
    main()
