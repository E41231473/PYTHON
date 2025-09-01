import cv2
import numpy as np

image = cv2.imread('Acara 4/gambar.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2], image.dtype) * 100

# operasi perkalian
citraPerkalian = cv2.multiply(gray, MatriksSatu)
filename = 'citraPerkalian.jpg'
cv2.imwrite(filename, citraPerkalian)
cv2.waitKey(0)
