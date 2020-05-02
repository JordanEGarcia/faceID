import cv2
import numpy as np

class Face:
    """
    Face class allows you to create a face object and automatically crop
    the image if it knows there is only one face. Saves Face Count as well
    """
    def __init__(self, fileName):
        self.fileName = fileName
        self.img = self.imread()
        self.faces = self.faces()
        self.faceCount = self.faceCount()
        self.cropped_img = self.cropImg()

    def imread(self):
        return cv2.imread(self.fileName, 0)

    def faceCount(self):
        return self.faces.shape[0]

    def cropImg(self):
        if self.faceCount==1:
            x, y, w, h = self.faces[0]
            crop_img = self.img[y: y + h, x: x + w]
            return crop_img

    def faces(self):
        face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
        return face_cascade.detectMultiScale(self.img, 1.3, 5)
