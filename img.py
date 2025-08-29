import cv2

path = r"C:\Users\syahb\Downloads\Logo_Polije.png"

img = cv2.imread(path)

if img is None:
    img = None
else:
    cv2.imshow("Logo Polije", img)

    cv2.waitKey(0)

    cv2.destroyAllWindows()



