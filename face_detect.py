import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade  = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

# Take in an image
#for now we'll do a test
gray = cv2.imread('test/will_smith.jpg', 0)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in faces:
    # Draw rectangle around the face
    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 255), 3)

cv2.waitKey(0)
cv2.destroyAllWindows()
