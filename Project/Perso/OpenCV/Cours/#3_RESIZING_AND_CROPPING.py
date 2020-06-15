import numpy as np
import cv2

img = cv2.imread("/Project/Perso/OpenCV/cards.jpg")
print(img.shape)

# Resize
imgResize = cv2.resize(img, (1000, 500))
print(imgResize.shape)

# Crop
imgCropped = img[200:500, 0:200]

cv2.imshow("Image", img)
cv2.imshow("Image resized", imgResize)
cv2.imshow("Image cropped", imgCropped)

cv2.waitKey(0)