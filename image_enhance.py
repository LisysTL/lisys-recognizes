# image_enhance.py
import numpy as np
import cv2
from skimage import exposure


def original(image):
    return image


def brightness(image): # use when Image Too Dark
    enhanced_image = cv2.equalizeHist(image)
    print('Image enhanced')
    return enhanced_image


def contrast(image):  # Use when Image Too Bright
    p2, p98 = np.percentile(image, (2, 98))
    image_contrast_stretched = exposure.rescale_intensity(image, in_range=(p2, p98))
    return image_contrast_stretched


def gamma_correction(image, threshold=127):  # Automatically brightens or darkens the image
    avg_intensity = cv2.mean(image)[0]

    if avg_intensity > threshold:
        gamma = 1.5
    else:
        gamma = 0.5
    image_gamma_corrected = exposure.adjust_gamma(image, gamma)
    return image_gamma_corrected


def reduce_motion_blur(image, kernel_size=(3, 3), blur_strength=5):  # Reduces Motion Blur, Increases Sharpness
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


def edge_detector(image):  # Canny Edge Detector
    edges = cv2.Canny(image, threshold1=100, threshold2=200)
    return edges


def skin_detection(image):  # Segments Skin from Images
    # Convert image to YCrCb color space
    ycrcb = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2YCrCb)
    # Define lower and upper bounds for skin color in YCrCb color space
    lower_skin = np.array([0, 133, 77], dtype=np.uint8)
    upper_skin = np.array([255, 173, 127], dtype=np.uint8)

    # Create a mask using the defined skin color range
    mask = cv2.inRange(ycrcb, lower_skin, upper_skin)

    # Apply morphological operations to remove noise
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=2)
    mask = cv2.dilate(mask, kernel, iterations=2)

    # Increase pixel values of skin regions
    result = cv2.bitwise_and(image, image, mask=mask)
    return result


def image_resizer(image):  # Resizes Image before enhancement
    width = 1600
    height = 900

    image = cv2.resize(image, (width, height))
    return image


def Image_Enchancer(image, threshold=127):  # Auto Enchancer

    # Calculate the average pixel intensity
    avg_intensity = cv2.mean(image)[0]

    # Check if the average intensity is above the threshold
    if avg_intensity > threshold:
        Enchanced_Image = contrast(image)

    else:
        Enchanced_Image = brightness(image)

    # Increasing Sharpness
    Enchanced_Image = reduce_motion_blur(image)
    return Enchanced_Image
