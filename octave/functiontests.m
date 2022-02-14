pkg load image;

system("clear");
clear all;

image = imread("../python/ImageProcessing/images/satellite-image.png");

m = rows(image)
n = columns(image)

noise = wgn(m, n, 0.2)
