#! /usr/bin/python
#  ______________________________________________________
# /\                                                     \
# \_| Filename    : dft2D.py                             |
#   | Maintainer  : Nikin Baidar                         |
#   | Description : Image Transformation                 |
#   |               (2D Discrete Fourier Transfomration) |
#   |   _________________________________________________|_
#    \_/___________________________________________________/

import numpy as np
import cv2
from matplotlib import pyplot


def DFT(intensity_image, shift=False):
    """ Discrete Fourirer transformation of intensity_images in spatial
    domain to images in frequency domain.
    * Args:
        intensity_image (numpy_array)
        shift (bool)
    """

    def getFrequency(u, v):
        """ Implementation of the Fourier transform. """
        sum = 0
        for x in range(M):
          for y in range(N):
            factor = np.exp(-1j * 2*np.pi * ((u * x)/M + (v * y)/N))  
            sum =  sum + intensity_image[x,y] * factor
        return sum

    M, N = intensity_image.shape[0], intensity_image.shape[1]

    # Init 
    magnitude = np.zeros_like(intensity_image, dtype=np.float64)
    angle = np.zeros_like(intensity_image, dtype=np.float64)

    for u in range(M):
        for v in range(N):
            frequency = getFrequency(u, v)
            magnitude[u, v] = np.sqrt( frequency.real**2 + frequency.imag**2)
            angle[u, v] = np.arctan2(frequency.imag, frequency.real) 

    if shift:
        shift_factor = [dim // 2 * (1) for dim in intensity_image.shape]
        shift_axes = (0, 1)
        magnitude = np.roll(magnitude, shift_factor, shift_axes)
        angle = np.roll(angle, shift_factor, shift_axes)

    return { 'magnitude': magnitude, 'angle' : angle }


def IDFT(frequency_image):
    """ Inverse discrete Fourirer transformation of intensity_images in
    spatial domain to images in frequency domain.
    * Args:
        frequency_image (numpy_array)
    """

    def getIntensity(u, v):
        """ Implementation of inverse Fourier transform. """
        sum = 0.0
        for x in range(M):
          for y in range(N):
            factor = np.exp(1j * 2*np.pi * ((u * x)/M + (v * y)/N))  
            sum += frequency_image[x,y] * factor
        return sum

    magnitude = frequency_image.get('magnitude')
    angle = frequency_image.get('angle')

    frequency_image = magnitude * np.exp(1j * angle)

    M, N = frequency_image.shape[0], frequency_image.shape[1]

    # Init output image
    spatial_domain = np.zeros_like(frequency_image, dtype=np.float64)

    for u in range(M):
        for v in range(N):
          intensity = getIntensity(u, v)
          brightness = np.abs(intensity)
          spatial_domain[u, v] = brightness

    spatial_domain = spatial_domain / (M*N)

    return spatial_domain


def spatial2frequency(intensity_image, shift=False):
    out_fft = np.fft.fft2(intensity_image)
    if shift:
        out_fft = np.fft.fftshift(out_fft) 

    magnitude = np.abs(out_fft)
    angle = np.angle(out_fft)

    frequency_domain = {
            'magnitude': magnitude,
            'angle' : angle
            }

    return frequency_domain


def frequency2spatial(frequency_image):
    """TODO: Docstring for frequency2spatial.
    :returns: TODO

    """
    magnitude = frequency_image.get('magnitude')
    angle = frequency_image.get('angle')

    # a + ib = r*exp(iθ)
    frequency_image = magnitude * np.exp(1j * angle)
    spatial_domain = np.abs(np.fft.ifft2(frequency_image))

    return spatial_domain


def main():

    # # Horizontal Frequency
    image = np.array([
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 1, 1, 0]],
        dtype=np.uint8)

    # Vertical Frequency
    # image = np.transpose(image)

    # image = cv2.imread('./images/Lenna_64x64.png', 0) 

    # Numpy
    module = "Numpy"
    frequency_domain = spatial2frequency(image, shift=True)
    spatial_domain = frequency2spatial(frequency_domain)

    # # Self implementation
    # module = "custom"
    # frequency_domain = DFT(image, shift=True) 
    # spatial_domain = IDFT(frequency_domain)

    #################
    # Visulizations #
    #################

    frequency_image = frequency_domain.get('magnitude')
    frequency_image = np.log(frequency_image + np.ones_like(frequency_image))

    figure, axes = pyplot.subplots(1, 3)
    axis = axes.flatten()
    axis[0].imshow(image, cmap='gray')
    axis[0].title.set_text('Original')

    
    axis[1].imshow(frequency_image, cmap='gray')
    axis[1].title.set_text('F domain')

    axis[2].imshow(spatial_domain, cmap='gray')
    axis[2].title.set_text('S domain')
    figure.suptitle(f"Frequency domain operations using {module} module.")

    pyplot.show()

if __name__ == '__main__':
    main()
