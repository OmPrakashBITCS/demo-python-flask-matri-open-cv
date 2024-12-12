# Load the image
import cv2 # type: ignore
from typing import List


def detect_face(image_paths: List[str]):
    total_faces: List[int] = []
    for image_path in image_paths:
        # Load the face detection cascade classifier
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

        # Load the image
        # img = cv2.imread(image_path)

        # Convert the image to grayscale
        gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image using the cascade classifier
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        total_faces.append(len(faces))

    return total_faces


def detect_face_with_bounding_boxes(image_paths: List[str]):
    all_faces = []
    for image_path in image_paths:
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        
        gray = cv2.cvtColor(image_path, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        all_faces.append(faces)

    return all_faces