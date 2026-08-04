import cv2
import numpy as np

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    h, w = frame.shape[:2]

    pts1 = np.float32([
        [100, 100],
        [w - 100, 100],
        [100, h - 100],
        [w - 100, h - 100]
    ])

    pts2 = np.float32([
        [50, 150],
        [w - 50, 50],
        [150, h - 50],
        [w - 150, h - 150]
    ])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    transformed = cv2.warpPerspective(frame, M, (w, h))

    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
