#! /usr/bin/octave

% Import modules
pkg load image;
pkg load statistics;

system("clear");
clear all;

% figure();

% Read an image
image = imread("../python/ImageProcessing/images/satellite-image.png") ;
image_gray = rgb2gray(image);
imshow(image_gray);
waitforbuttonpress();

M = rows(image_gray);
N = columns(image_gray);

% Rayleigh Distribution
% noise = raylrnd(0.5, [M, N]);
% noisy_image = image_gray .* noise;
% imshow(noisy_image);
% waitforbuttonpress();

% Using built in function
noisy_image = imnoise(image_gray, "speckle");
imshow(noisy_image);

imhist(noisy_image);
xlabel("Pixels");
ylabel("Count");

waitforbuttonpress();
