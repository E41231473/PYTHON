import cv2

image = cv2.imread('Minggu 1/img/uno.png')

imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

filename1 = 'CitraGray.png'
cv2.imwrite(filename1, imgGray)

cv2.imshow("Asli", image)
cv2.imshow("Grayscale", imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()