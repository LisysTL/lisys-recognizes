# face_detect.py
import face_recognition

def detect_faces(image):
    # Find all face locations in the image
    face_locations = face_recognition.face_locations(image)

    # Return the face locations
    return face_locations
