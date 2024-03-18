# face_recognize_app.py
import os
import cv2
import numpy as np
import streamlit as st
from PIL import Image
from face_recognize import recognize_faces, get_encodings

# from util import set_background

# set_background('pix/4.png')

def recognize_faces_in_image(uploaded_image, list_encodings, list_names):
    try:
        # Convert uploaded image to OpenCV format
        img = Image.open(uploaded_image)
        img_cv0 = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        img_cv = cv2.cvtColor(np.array(img_cv0), cv2.COLOR_BGR2RGB)

        # Recognize faces in the image
        recognized_faces = recognize_faces(img_cv, list_encodings, list_names)

        # Draw rectangles around recognized faces
        for name, (top, right, bottom, left) in recognized_faces.items():
            cv2.rectangle(img_cv, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(img_cv, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Display the image with detected and recognized faces
        st.image(img_cv, caption='Image with Detected and Recognized Faces', use_column_width=True)
    except Exception as e:
        st.error("Error recognizing faces: {}".format(str(e)))

def main():
    st.title("Face Recognition")

    # Set the path to your image dataset
    dataset_path = 'v2r2aliy pix'
    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith('.jpg')]

    # Get encodings and names from the image dataset
    list_encodings, list_names = get_encodings(image_paths)

    # Upload an image to recognize faces
    uploaded_image = st.file_uploader("Upload JPG Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        recognize_faces_in_image(uploaded_image, list_encodings, list_names)

if __name__ == "__main__":
    main()
