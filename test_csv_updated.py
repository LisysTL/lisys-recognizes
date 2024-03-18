
#### 

# Contains error have to fix

###








import os
import cv2
import numpy as np
import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from face_recognize import recognize_faces, get_encodings

def display_csv():
    st.title("Read CSV File")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])

    if uploaded_file is not None:
        # Read CSV file into DataFrame
        df = pd.read_csv(uploaded_file)

        # Display DataFrame
        st.write("CSV file content:")
        st.dataframe(df)

def recognize_and_display():
    st.title("Face Recognition")

    # Upload an image to be recognized
    uploaded_image = st.file_uploader("Upload Image", type=['jpg', 'jpeg'])

    if uploaded_image is not None:
        try:
            # Convert uploaded image to OpenCV format
            img = Image.open(uploaded_image)
            img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
        except Exception as e:
            st.error("Error converting image: {}".format(str(e)))
            return

        # Display the uploaded image
        st.image(img, caption='Uploaded Image', use_column_width=True)

        # Perform face recognition
        list_encodings, list_names = get_encodings(image_paths)
        recognized_faces = recognize_faces(img_cv, list_encodings, list_names)

        # Generate a new CSV file name
        csv_file_name = "recognized_faces.csv"

        # Create DataFrame from recognized faces
        df = pd.DataFrame.from_dict(recognized_faces, orient='index', columns=['Location'])

        # Write DataFrame to CSV file
        df.to_csv(csv_file_name, index_label='Name')

        # Display recognized faces as CSV
        st.write("Recognized Faces:")
        st.dataframe(df)

def main():
    st.sidebar.title("Options")
    app_mode = st.sidebar.selectbox("Choose the app mode", ["View CSV", "Generate CSV"])

    if app_mode == "View CSV":
        display_csv()
    elif app_mode == "Generate CSV":
        recognize_and_display()

if __name__ == "__main__":
    main()
