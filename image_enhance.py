# Classroom Image Enhancer
"""
How to use :-
1. call the Image Enhancer function from the file.
Example :- import image_enhance as ie

2. Apply Function on images.
Example:- result = ie.Image_Enhancer(image_path)

3. The Function automatically reads the image and converts it into grayscale for Enhancement.

4. Do not use this Function on Detected Images.
"""

import cv2
import numpy as np
from skimage import exposure


def gamma_correction(image, threshold=127):  # Automatically brightens or darkens the image
    avg_intensity = cv2.mean(image)[0]

    if avg_intensity > threshold:
        gamma = 1.5
    else:
        gamma = 0.5
    image_gamma_corrected = exposure.adjust_gamma(image, gamma)
    return image_gamma_corrected


def reduce_motion_blur(image, kernel_size=(2, 2), blur_strength=2):  # Reduces Motion Blur, Increases Sharpness
    # Create motion blur kernel
    kernel = np.zeros(kernel_size)
    kernel[int((kernel_size[0] - 1) / 2), :] = np.ones(kernel_size[0])
    kernel /= kernel_size[0]

    # Apply Wiener deconvolution
    psf = np.ones((5, 5)) / 25  # Point spread function (PSF)
    deconvolved = cv2.filter2D(image, -1, psf)
    deconvolved = cv2.warpAffine(deconvolved, np.float32([[1, 0, 0], [0, 1, 0]]), (image.shape[1], image.shape[0]))

    # Add a fraction of the residual back to the image
    deconvolved = cv2.addWeighted(image, 1.0 + blur_strength, deconvolved, -blur_strength, 0)

    return deconvolved


def Image_Enhancer(image):  # Auto Enhancer

    image = cv2.imread(image, cv2.IMREAD_GRAYSCALE)  # Reading and Grayscale Conversion
    image = cv2.resize(image, (1550, 850))  # Resizing

    Enhanced_Image = gamma_correction(image)  # Brightness and Contrast
    Enhanced_Image = reduce_motion_blur(Enhanced_Image)  # Blur and Sharpen
    return Enhanced_Image
