import cv2
import numpy as np

image = cv2.imread('Acara 4/gambar.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2], image.dtype) * 100

# operasi pembagian
citraPembagian = cv2.divide(gray, MatriksSatu)
filename = 'citraPembagian.jpg'
cv2.imwrite(filename, citraPembagian)
cv2.waitKey(0)
