import cv2
import numpy as np

face_detector = cv2.CascadeClassifier('data/cascade/haarcascade_frontalface_default.xml')
eye_detector  = cv2.CascadeClassifier('data/cascade/haarcascade_eye.xml')

# Take in an image
#for now we'll do a test
cap = cv2.imread('test/will_smith.jpg')


gray = cv2.cvtColor(cap, cv2.COLOR_BGR2GRAY)
#faces = face_detector.detectMultiScale(img, 1.3, 5)

cv2.imshow("will_smith", cap)

cv2.waitKey(0)
cv2.destroyAllWindows()
