# Libs
import cv2
import numpy as np

capture = cv2.VideoCapture(0) # Get's the video input at index 0

# Classifiers trained for facial detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")

while True:
    ret, frame = capture.read()

    # Converting to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Params: base image, scaleFactor, minNeighbors, minSize
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, width, height) in faces:
        # Draws a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+width, y+height), (0, 0, 255), 3)
        roi_gray = gray[y:y+width, x:x+width]
        roi_color = frame[y:y+height, x:x+width]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5) # Detects the eyes
        for (ex, ey, ewidth, eheight) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ewidth, ey+eheight), (0, 255, 0), 3)


    cv2.imshow('Video', frame)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()