# enhance_image_app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from image_enhance import enhance_image

# from util import set_background

# set_background('pix/1.png')

def enhance_uploaded_image(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        # img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Enhance the image
        enhanced_image = enhance_image(img)

        # Display the enhanced image
        st.image(enhanced_image, caption='Enhanced Image', use_column_width=True)
    except Exception as e:
        st.error("Error enhancing image: {}".format(str(e)))

def main():
    st.title("Image Enhancement")

    # Upload an image to be enhanced
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        enhance_uploaded_image(uploaded_image)

if __name__ == "__main__":
    main()
