import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8) # Créé une matrices de 512x512

# print(img)
img[0:254, 0:254] = 255, 0, 0 # colore la matrice

cv2.line(img, (0, 0), (512, 512), (0, 0, 255), 3)   # Trace une ligne
cv2.rectangle(img, (254, 254), (512, 512), (0, 255, 0), 2) # Rectangle
cv2.circle(img, (254, 254), 64, (255, 255, 0), 5)

cv2.putText(img, "OPENCV", (254, 254), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 155, 0), 1)

cv2.imshow("Box", img)

cv2.waitKey(0)