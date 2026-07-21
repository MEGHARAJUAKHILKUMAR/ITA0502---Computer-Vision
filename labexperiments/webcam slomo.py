import cv2

# Open the webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

speed = 30   # Normal speed (milliseconds)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Display the webcam video
    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(speed) & 0xFF

    # Press 's' for slow motion
    if key == ord('s'):
        speed = 100

    # Press 'f' for fast motion
    elif key == ord('f'):
        speed = 10

    # Press 'n' for normal speed
    elif key == ord('n'):
        speed = 30

    # Press 'q' to quit
    elif key == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Webcam video processing completed successfully.")
