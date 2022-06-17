import cv2 as cv
import numpy as np
import os

image = np.array([
    [5, 5 , 5, 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5],
    [5, 5 , 5, 5 , 5 , 5 , 5 , 11, 11, 11, 11, 5 , 5 , 5 , 5],
    [5, 5 , 5, 5 , 11, 11, 1 , 15, 7 , 7 , 7 , 7 , 11, 5 , 5],
    [5, 5 , 5, 7 , 7 , 11, 1 , 1 , 11, 7 , 7 , 7 , 7 , 15, 5],
    [5, 5 , 7, 7 , 7 , 11, 1 , 1 , 15, 7 , 7 , 7 , 7 , 11, 5],
    [5, 11, 7, 7 , 7 , 7 , 1 , 1 , 1 , 7 , 7 , 7 , 7 , 11, 5],
    [5, 11, 7, 7 , 7 , 7 , 15, 1 , 1 , 11, 7 , 7 , 7 , 15, 5],
    [5, 11, 7, 7 , 7 , 7 , 11, 1 , 1 , 11, 7 , 7 , 11, 5 , 5],
    [5, 5 , 7, 7 , 7 , 7 , 7 , 1 , 1 , 11, 7 , 1 , 5 , 5 , 5],
    [5, 5 , 5, 11, 7 , 7 , 7 , 11, 15, 11, 5 , 5 , 5 , 5 , 5],
    [5, 5 , 5, 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5 , 5]])

# Init an empyt list
m, n = image.shape[0], image.shape[1]

def resetCounter_UpdateList():
    global current_pixel_count

    pixels.append(current_pixel_count)
    pixels.append(current_pixel)
    current_pixel_count = 1

pixels = []

for i in range(m):
    current_pixel_count = 1
    for j in range(n):
        current_pixel = image[i,j]
        try:
            next_pixel = image[i, j+1]
            if next_pixel == current_pixel:
                current_pixel_count += 1
            else:
                resetCounter_UpdateList()
                # print(pixels)
                # input()
    
        except: # end of row
            resetCounter_UpdateList()
            # print(pixels)
            # input()

        os.system('clear')
        # print(f'Current:{current_pixel} ; Next:{next_pixel}, ; Count:{current_pixel_count}')
        # input()

## append the original shape for decompressoion;
compressed = [m, n]
compressed.extend(pixels)
compressed = np.array(compressed)
print(compressed)
