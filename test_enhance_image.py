
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import image_enhance as ie

# from util import set_background

# set_background('pix/1.png')
def original(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)

        # Enhance the image
        enhanced_image = ie.original(img)

        # Display the enhanced image
        st.image(enhanced_image, caption='Original Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))


def brightness(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.brightness(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Brightend Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def contrast(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.contrast(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Darkend Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))


def gamma(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.gamma_correction(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Gamma Corrected Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def edge(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.edge_detector(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Edges Detected', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))



def motion(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.reduce_motion_blur(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Sharpened Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def skin(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        # img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Enhance the image
        enhanced_image = ie.skin_detection(img)

        # Display the enhanced image
        st.image(enhanced_image, caption='Skin Detected Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))


def custom(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.Image_Enchancer(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Enchanced Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def resize(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.image_resizer(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Resized Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def main():
    st.title("Image Enhancement")

    # Upload an image to be enhanced
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        operation = st.selectbox('Choose an operation',['Original','Auto Enhancer','Bright', 'Contrast', 'Gamma Correction', 'Sharpness','Skin Detector', 'Edge Detector','Resize'])

        if operation == 'Bright':
            brightness(uploaded_image)

        elif operation == 'Contrast':
            contrast(uploaded_image)
        
        elif operation == 'Auto Enhancer':
            custom(uploaded_image)

        elif operation == 'Gamma Correction':
            gamma(uploaded_image)

        elif operation == 'Sharpness':
            motion(uploaded_image)

        elif operation == 'Skin Detector':
            skin(uploaded_image)

        elif operation == 'Edge Detector':
            edge(uploaded_image)

        elif operation == 'Resize':
            resize(uploaded_image)

        elif operation == 'Original':
            original(uploaded_image)


if __name__ == "__main__":
    main()
