#!/usr/bin/env python

import cv2 as cv
import numpy as np

from convolution import pause
from entropy import getHist

def main():
    src = cv.imread("/home/nikin/downloads/viber_downloads/workonthis.jpg",
            cv.IMREAD_GRAYSCALE) 
    # src = cv.imread("./images/Lenna.png", cv.IMREAD_GRAYSCALE) 

    rows, columns = src.shape[0], src.shape[1]
    image_resolution = rows * columns
    
    src_hist = getHist(src) ; L = len(src_hist)
    pixel_probability = [src_hist[i] / image_resolution for i in range(0, L)]

    intraClassVariance = 1000000 # Large random value 
    optimum_threshold = -1

    ############################################

    def getIntraCLassVariance(threshold):
        bg_probability = [pixel_probability[i] for i in range(0, threshold-1) ]
        fg_probability = [pixel_probability[i] for i in range(threshold, L) ]

        bg_weight, fg_weight = sum(bg_probability), sum(fg_probability)

        bg_mean = sum([ bg_probability[i] * src_hist[i] / bg_weight 
            for i in range (0, threshold-1) ])

        fg_mean = sum([ fg_probability[i-threshold] * src_hist[i] / fg_weight
            for i in range (threshold, L) ])

        bg_variance = sum([ bg_probability[i] * (src_hist[i] * bg_mean)**2 / bg_weight
            for i in range (0, threshold-1) ])

        fg_variance = sum([ fg_probability[i-threshold] * 
            (src_hist[i] * fg_mean)**2 / fg_weight
            for i in range (threshold, L) ])

        return (bg_weight * bg_variance + fg_weight * fg_variance)

    # print(getIntraCLassVariance(24))

    for i in range(24,L):
        current_variance = getIntraCLassVariance(i)
        if i == 24:
            intraClassVariance = current_variance
        elif current_variance < intraClassVariance:
            intraClassVariance = current_variance
            optimum_threshold = i

    print(optimum_threshold)

    for i in range(rows):
        for j in range(columns):
            if src[i,j] < optimum_threshold:
                src[i,j] = 0
            else:
                src[i,j] = 1

    cv.imshow("Processed", src)
    pause()



    ############################################

if __name__ == "__main__":
    main()
