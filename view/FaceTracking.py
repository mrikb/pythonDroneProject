import cv2
import numpy as np

def findFace(img):
    faceCascasde = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
    imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascasde.detectMultiScale(imgGrey, 1.2, 8)

    myFaceListC = []
    myFaceListArea = []

    for (x, y, w ,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)


cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    findFace(img)
    cv2.imshow("Output", img)
    cv2.waitKey(1)

