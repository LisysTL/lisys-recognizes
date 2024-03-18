# face_recognize.py
import os
import cv2
import numpy as np
import face_recognition

def get_encodings(paths):
    print('{} images found'.format(len(paths)))
    list_encodings = []
    list_names = []

    for img_path in paths:
        img = cv2.imread(img_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB
        (name, _) = os.path.splitext(os.path.basename(img_path))
        face_encodings = face_recognition.face_encodings(img)
        if face_encodings:
            list_encodings.append(face_encodings[0])
            list_names.append(name)
        else:
            print('Could not detect the face from image', img_path)

    return list_encodings, list_names

def recognize_faces(image, list_encodings, list_names, tolerance=0.5):  # tolerance is confidence , change it for seing variations in results
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(img_rgb)
    face_encodings = face_recognition.face_encodings(img_rgb, face_locations)

    recognized_faces = {}  # Dictionary to store recognized faces

    for encoding, location in zip(face_encodings, face_locations):
        matches = face_recognition.compare_faces(list_encodings, encoding, tolerance=tolerance)
        name = 'Not identified'
        face_distances = face_recognition.face_distance(list_encodings, encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = list_names[best_match_index]
        recognized_faces[name] = location  # Store recognized face with location

    return recognized_faces