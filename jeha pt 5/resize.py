import cv2
import numpy as np
import os

#buka gambar
img_path = os.path.join(".","img/karakter.png")
img = cv2.imread(img_path)

(hight, width) = img.shape[:2]
center = (width // 1080, hight // 720)

r = 150.0 / width
dim = (150, int(hight * r))

matrix = cv2.getRotationMatrix2D(center, 45, 1.0)
rotated = cv2.warpAffine(img, matrix, (width, hight))

rotated = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)  

cv2.imshow("Rotated", rotated)
cv2.imshow("Resized", rotated)
cv2.waitKey(50000)  