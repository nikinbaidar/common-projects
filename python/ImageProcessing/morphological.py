#!/usr/bin/env python

import numpy as np
import cv2 as cv
from copy import deepcopy
from spatial_filtering import addPadding, removePadding
from convolution import pause

def erode(image, structuring_element, addBorder=False, iterations=1):
    
    if addBorder:
        image = addPadding(image)
        removeBorder = True
    else:
        removeBorder = False

    result_img = deepcopy(image)

    for i in range(iterations):
        k = structuring_element.shape[0]
        structuring_element_size = k // 2
        m,n = image.shape[0], image.shape[1]
        for x in range(m):
            for y in range(n):
                if x+k > m or y+k > n:
                    continue
                pixels = image[x:x+k, y:y+k]
                if not (pixels == structuring_element).all():
                    result_img[x+structuring_element_size , 
                            y+structuring_element_size] = np.min(pixels)
                # print(result_img, sep='\n'*2, end='\n'*2)
                # input()

        image = deepcopy(result_img)

    if removeBorder:
        result_img = removePadding(result_img)

    return result_img


def dilute(image, structuring_element):
    def getAnchor(m,n):
        if 1 & m:
            m = m // 2
            return (m, m)
        else:
            return (0,0)

    k = structuring_element.shape[0]
    structuring_element_size = k // 2
    m,n = image.shape[0], image.shape[1]
    result_img = deepcopy(image)
    for x in range(m):
        for y in range(n):
            if x+k > m or y+k > n:
                continue
            pixels = image[x:x+k, y:y+k]
            anchor = getAnchor(pixels.shape[0],pixels.shape[1])
            a,b = anchor[0], anchor[1]
            if (pixels[a,b] == structuring_element[a,b]):
                print(result_img[x:x+3, y:y+2]) #= structuring_element
                input()

            # print(result_img, sep='\n'*2, end='\n'*2)
            # input()

    # image = deepcopy(result_img)

    # if removeBorder:
    #     result_img = removePadding(result_img)

    return result_img


def main():
   # Wikipedia example: 
   # src = np.array([
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],        
   #     [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],    
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],    
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],                
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],        
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],    
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],    
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],   
   #     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
   #     ], dtype=np.uint8)

   src = (cv.imread("./images/L_inverted.jpg", 0) / 255.0)
   kernel = np.ones((3,3), np.uint8)

   # dilute(src, filter)

   # eroded_outcome = erode(src, kernel, iterations=1)
   # print("Output of custom fucntion without zero-padding:")
   # print(eroded_outcome)
   # print()

   # cv2_eroded_outcome = cv.erode(src, kernel)

   eroded_outcome = erode(src, kernel, addBorder=True, iterations=4)
   # eroded_outcome = np.array(eroded_outcome, dtype=np.uint8)
   # print("Output of custom fucntion with zero-padding:")
   # print(eroded_outcome)
   # print()

   dilation_output = dilute(src, kernel)
   # eroded_outcome = np.array(eroded_outcome, dtype=np.uint8)
   # print("Output of custom fucntion with zero-padding:")
   # print(eroded_outcome)
   # print()

   # print("Output of cv2.erode with indifferent padding:")
   # print(cv2_eroded_outcome)

   # cv.imshow("Output of erosion using custom fucntion", eroded_outcome)
   # cv.imshow("Output of erosion using built-in function", cv2_eroded_outcome)
   # cv.imshow("Input", src)

   cv.imshow("Output of dilation using custom fucntion", dilation_outcome)
   # cv.imshow("Output of dilation using built-in function", cv2_eroded_outcome)
   cv.imshow("Input", src)
   pause()

if __name__ == '__main__':
    main()

