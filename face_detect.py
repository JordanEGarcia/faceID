import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')

# Take in an image
#for now we'll do a test
gray = cv2.imread('test/will_smith.jpg', 0)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Crop a single face from an image.
def faceID():
    # Count how many faces
    faceCount = faces.shape[0]
    if faceCount==1:
        x, y, w, h = faces[0]
        crop_img = gray[y: y + h, x: x + w]
        cv2.imwrite("test/face.jpg", crop_img)
        return True
    else:
        return False
faceID()

cv2.waitKey(0)
cv2.destroyAllWindows()
