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


def Enhanced(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2GRAY)

        # Enhance the image
        enhanced_image = ie.Image_Enhancer(img_cv)

        # Display the enhanced image
        st.image(enhanced_image, caption='Enchanced Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))


def main():
    st.title("Image Enhancement")

    # Upload an image to be enhanced
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        operation = st.selectbox('Choose an operation', ['Original', 'Auto Enhancer'])

        if operation == 'Original':
            original(uploaded_image)

        elif operation == 'Auto Enhancer':
            Enhanced(uploaded_image)


if __name__ == "__main__":
    main()