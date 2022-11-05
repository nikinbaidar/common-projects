#!/usr/bin/env python

import cv2
import numpy as np
import random

a  = np.array([np.arange(1,4), np.arange(4,7), np.arange(7,10)])
# b  = np.transpose(np.array([np.arange(1,4), np.arange(4,7), np.arange(7,10)]))
# print(a)

# non_edge = np.where(a >= 5)

# a[non_edge[0], non_edge[1]] = 0

print(a)
# print()
# print(x, y)

# print()

# print(a/b)

# print()

# print(np.arctan(a/b))

# print(np.radians(-90) )
# print((-90 % 180), np.radians(-90 % 180))
# print()
# print(np.radians(-107.91936))
# print(np.radians(-107.91936 % 180))
# print()
# print(np.radians(107.91936))
# print((107.913946 % 180), np.radians(107.91936 % 180))
# print()
# print(np.radians(-90 % 360) )
# print(np.radians(270))

# print()
# x = random.randint(0, 180)
# print(x, x % 180)

####################################

# def replicateBorder(image, depth=1):
#     # h_pad -> x = add columns 
#     # v_pad -> y = add rows
#     print(image.shape)
#     for i in range(depth):
#         x, y = image.shape[0], image.shape[1]
#         h_pad_left = image[:,0].reshape(-1,1)
#         h_pad_right = image[:,-1].reshape(-1,1)
#         v_pad_up = np.hstack(([0], image[0,:], [0]))
#         v_pad_down = np.hstack(([0], image[-1,:], [0]))
#         image = np.hstack((h_pad_left, image, h_pad_right))
#         image = np.vstack((v_pad_up, image, v_pad_down))
#     return image

# src = np.array([
#     [0, 0, 0, 0, 2, 0, 0, 0],
#     [0, 1, 1, 1, 1, 0, 0, 1],    
#     [0, 1, 1, 1, 1, 0, 0, 1],   
#     [1, 1, 1, 1, 1, 1, 1, 1], 
#     [0, 1, 1, 1, 1, 1, 1, 1], 
#     [0, 1, 1, 0, 0, 0, 1, 1], 
#     [0, 1, 1, 0, 0, 0, 1, 1], 
#     [0, 0, 0, 0, 7, 0, 0, 9]
#     ])

# replicateBorder(src)

ranges = {
            (0, 22.5)      : 0,
            (157.5, 181)   : 0,
            (22.5, 67.5)   : 45,
            (67.5, 112.5)  : 90,
            (112.5, 157.5) : 135,
        }

def remapTheta(value):
    value = int(np.ceil(value)) % 180
    for boundary in ranges.keys():
        if (boundary[0] <= value) and (value < boundary[1]):
            mapping = ranges[boundary]
            return mapping

# for value in [306.435, 67.93024, 131.432423, -107.91936, 47.0423, -90, 180, 14.304]:
#     print(value, "->",  remapTheta(value))
