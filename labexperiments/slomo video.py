import cv2

video = cv2.VideoCapture(r"D:\15894472_3840_2160_30fps.mp4")

while video.isOpened():
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    key = cv2.waitKey(30) & 0xFF

    if key == ord('s'):
        cv2.waitKey(100)
    elif key == ord('f'):
        cv2.waitKey(10)
    elif key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

print("Video processing completed successfully.")
