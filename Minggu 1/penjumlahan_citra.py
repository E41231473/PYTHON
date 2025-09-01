import cv2
import numpy as np

image = cv2.imread('Minggu 1/img/uno.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
MatriksSatu = np.ones(image.shape[:2], image.dtype) * 100

citraPenjumlahan = cv2.add(gray, MatriksSatu)

filename1 = 'Citra1.jpg'
filename2 = 'Citra2.jpg'
filename3 = 'CitraPenjumlahan.jpg'

cv2.imwrite(filename1, gray)
cv2.imwrite(filename2, MatriksSatu)
cv2.imwrite(filename3, citraPenjumlahan)
cv2.waitKey(0)
