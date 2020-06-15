import cv2
import numpy as np

img = cv2.imread("/Project/Perso/OpenCV/cards.jpg")

width, height = 250, 350
pts1 = np.float32([[225, 95], [425, 140], [165, 380], [365, 425]])
pts2 = np.float32([[0, 0], [width, 0], [0, height], [width, height]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Image", img)
cv2.imshow("Card", imgOutput)
cv2.waitKey(0)
