#!/usr/bin/env python

import numpy as np
import cv2 as cv
import convolution
import matplotlib.pyplot as plt
from skimage.feature import canny,peak_local_max
from skimage.segmentation import watershed
from skimage.color import rgb2gray
import scipy.ndimage as nd
plt.rcParams["figure.figsize"] = (12,8)
 
# load images and convert grayscale
src = cv.imread("./images/stock-photo.duckduckgo.com.jpg", 0)
 
thresh = cv.threshold(src, 0, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)[1]

# Since, the contrast difference is not much
plt.imshow(thresh)
plt.title('thresh')
plt.show()

distance_map = nd.distance_transform_edt(thresh)
local_max = peak_local_max(distance_map, min_distance=20, labels=thresh)

# Perform connected component analysis then apply Watershed
# markers = nd.label(local_max, structure=np.ones((3, 3)))[0]
# labels = watershed(-distance_map, markers, mask=thresh)

mask = np.zeros_like(distance_map, dtype=bool)
mask[tuple(local_max.T)] = True
markers, _ = nd.label(mask)
new = watershed(-distance_map, markers, mask=src)

fig, axes = plt.subplots(ncols=3, figsize=(9, 3), sharex=True, sharey=True)
ax = axes.ravel()

ax[0].imshow(src, cmap=plt.cm.gray)
ax[0].set_title('Original Input')
ax[1].imshow(-distance_map, cmap=plt.cm.gray)
ax[1].set_title('Distances')
ax[2].imshow(new, cmap=plt.cm.nipy_spectral)
ax[2].set_title('Separated objects')

for a in ax:
    a.set_axis_off()

fig.tight_layout()
plt.show()

# # Iterate through unique labels
# total_area = 0
# for label in np.unique(labels):
#     if label == 0:
#         continue

#     # Create a mask
#     mask = np.zeros(gray.shape, dtype="uint8")
#     mask[labels == label] = 255

#     # Find contours and determine contour area
#     cnts = cv.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = cnts[0] if len(cnts) == 2 else cnts[1]
#     c = max(cnts, key=cv2.contourArea)
#     area = cv2.contourArea(c)
#     total_area += area
#     cv2.drawContours(image, [c], -1, (36,255,12), 4)

# Perform watershed region segmentation
# segmentation = morphology.watershed(edges_sobel, markers)

 
# plt.imshow(segmentation)
# plt.title('Watershed segmentation')
 
# # plot overlays and contour
# segmentation = nd.binary_fill_holes(segmentation - 1)
# label_rock, _ = nd.label(segmentation)
# # overlay image with different labels
# image_label_overlay = label2rgb(label_rock, image=src)
 
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(24, 16), sharey=True)
# ax1.imshow(src)
# ax1.contour(segmentation, [0.8], linewidths=1.8, colors='w')
# ax2.imshow(image_label_overlay)
 
# fig.subplots_adjust(**margins)
