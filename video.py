import cv2

path = r"C:\Users\syahb\Downloads\Chinese Gong.mp4"

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Video tidak ditemukan.")
else:
    while True:
        ret, frame = cap.read()  
        if not ret:              
            break

        cv2.imshow("😑", frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()




