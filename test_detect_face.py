# detect_faces_app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
from face_detect import detect_faces

# from util import set_background

# set_background('pix/2.png')

def detect_faces_in_image(uploaded_image):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv0 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img_cv = cv2.cvtColor(np.array(img_cv0), cv2.COLOR_BGR2RGB)

        # Detect faces in the image
        face_locations = detect_faces(img_cv)

        # Draw rectangles around detected faces
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(img_cv, (left, top), (right, bottom), (0, 255, 0), 3)

        # Display the image with detected faces
        st.image(img_cv, caption='Image with Detected Faces', use_column_width=True)
    except Exception as e:
        st.error("Error detecting faces: {}".format(str(e)))

def main():
    st.title("Face Detection")

    # Upload an image to detect faces
    uploaded_image = st.file_uploader("Upload JPG Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        detect_faces_in_image(uploaded_image)

if __name__ == "__main__":
    main()
