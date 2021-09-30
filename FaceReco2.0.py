import cv2
import face_recognition
import os
import pyttsx3
import numpy as np

cap = cv2.VideoCapture(0)
knowFaces = []
knowNames = ["Alecita", "Mamá", "Papá", "Marco", "Wilfredo Tablero", "Anny","Tía"]
s = pyttsx3.init()
matches = []

while True:

    success, image = cap.read()
    for name in os.listdir("Images"):
        faces = face_recognition.load_image_file(f"Images/{name}")
        #print(name)
        encoding = face_recognition.face_encodings(faces)[0]
        knowFaces.append(encoding)
        
    face_location = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image)
    #Si alguien esta en la puerta
    
    for (top, right, bottom, left), face_encodings in zip(face_location, face_encodings):
        matches = face_recognition.compare_faces(knowFaces, face_encodings)
        face_distances = face_recognition.face_distance(knowFaces, face_encodings)
        best = np.argmin(face_distances)
    try:
        if matches[best]:
            name = knowNames[best]
            s.say(f"{name} esta en la puerta")
            s.runAndWait()
            break
        else :
            s.say("Alguien esta tocando la puerta")
            s.runAndWait()
            break
    except NameError as e:
        s.say("Alguien esta tocando la puerta pero no detecto a nadie afuera")
        s.runAndWait()
        pass
        break