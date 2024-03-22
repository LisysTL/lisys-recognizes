# detect_faces_app.py
import streamlit as st
import cv2
import numpy as np
from PIL import Image
import face_detect  as fd
from util import set_background


# from util import set_background



def main():
    st.title("Face Detection")

    # st.sidebar.title("Modules")
    # selected_module = st.sidebar.selectbox("Face Detection Module", ["Face locations", "MTCNN", "Dlib", "YOLO V3", "YOLO V4"])

    # Upload an image to detect faces
    uploaded_image = st.file_uploader("Upload JPG Image", type=['jpg', 'jpeg','png','webp'])

    
    if st.button('Face locations'):
        set_background('pix/1.png')
        fd.detect_faces_in_image(uploaded_image)

    if st.button('YOLO V3'):
        set_background('pix/3.png')
        fd.detect_faces_in_image_2(uploaded_image)

    if st.button('Dlib'):
        set_background('pix/4.png')
        fd.detect_faces_in_image_3(uploaded_image)




if __name__ == "__main__":
    main()
