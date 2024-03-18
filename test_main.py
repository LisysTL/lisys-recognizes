
# main.py
import os
import cv2
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from image_enhance import enhance_image
from face_detect import detect_faces
from face_recognize import recognize_faces, get_encodings

# from util import set_background


# set_background('pix/5.png')

# Function to display recognized faces in a tabular format
def display_recognized_faces(recognized_faces, list_names):
    df = pd.DataFrame(columns=["Name", "Status"])

    absent_count = 0
    present_count = 0

    for name in list_names:
        if name in recognized_faces:
            status = "Present"
            present_count += 1
        else:
            status = "Absent"
            absent_count += 1
        df = df.append({"Name": name, "Status": status}, ignore_index=True)

    st.write("Recognition Results:")
    st.dataframe(df)

    st.write(f"Total Students: {len(list_names)}")
    st.write(f"Present: {present_count}")
    st.write(f"Absent: {absent_count}")

def main():
    # Set the path to your image dataset
    st.title("Lisys Recognizes")

    dataset_path = 'v2r2aliy pix'
    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith('.jpg')]

    # Get encodings and names from the image dataset
    list_encodings, list_names = get_encodings(image_paths)

    # Upload an image to be recognized
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        try:
            # Convert uploaded image to OpenCV format
            img = Image.open(uploaded_image)
            img_cv = np.array(img)
        except Exception as e:
            st.error("Error converting image: {}".format(str(e)))
            return

        # Display the uploaded image
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Enhance the original image
        enhanced_image = enhance_image(img_cv)

        # Detect faces in the enhanced image
        face_locations = detect_faces(enhanced_image)

        # Recognize faces in the detected faces
        recognized_faces = recognize_faces(enhanced_image, list_encodings, list_names)

        # Display the recognized faces in a tabular format
        display_recognized_faces(recognized_faces, list_names)

if __name__ == "__main__":
    main()
