import cv2
import numpy as np

image = cv2.imread("Minggu 1/img/uno.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
Matriks = np.ones(image.shape[:2], image.dtype) * 255
citraNegatif = Matriks - gray

filename1 = 'CitraNegatif.jpg'
cv2.imwrite(filename1, citraNegatif)
cv2.waitKey(0)
