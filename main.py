# main.py
import os
import cv2
from image_enhance import enhance_image
from face_detect import detect_faces
from image_align import align_image
from face_recognize import recognize_faces, get_encodings
from excel_sheet_update import update_excel_sheet

def main():
    # Set the path to your image dataset
    dataset_path = 'v2r2aliy pix'
    image_paths = [os.path.join(dataset_path, f) for f in os.listdir(dataset_path) if f.endswith('.jpg')]

    # Get encodings and names from the image dataset
    list_encodings, list_names = get_encodings(image_paths)

    # Load an image to be recognized
    test_image_path = 'grp.jpg'
    test_image = cv2.imread(test_image_path)

    # Enhance the original image
    enhanced_image = enhance_image(test_image)

    # Detect faces in the enhanced image
    face_locations = detect_faces(enhanced_image)
    
    align_image()

    # Recognize faces in the detected faces
    recognized_faces = recognize_faces(enhanced_image, list_encodings, list_names)

    # Update Excel sheet with recognized faces
    update_excel_sheet(recognized_faces, list_names)

if __name__ == "__main__":
    main()
