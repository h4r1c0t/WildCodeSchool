import numpy as np
import cv2

# %% IMG
img = cv2.imread("D:/Github/Wild Code School/Project/OpenCV/cards.jpg")
cv2.imshow("Image", img)
cv2.waitKey(0)

# %% VIDEO
cap = cv2.VideoCapture("path")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break

# %% WEBCAM
cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

while True:
    success, img = cap.read()
    cv2.imshow("Web cam", img)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
