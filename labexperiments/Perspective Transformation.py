import cv2
import numpy as np

image = cv2.imread("micky.jpg")

rows, cols = image.shape[:2]

pts1 = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

pts2 = np.float32([
    [10, 100],
    [300, 50],
    [100, 300],
    [280, 280]
])

M = cv2.getPerspectiveTransform(pts1, pts2)

perspective_image = cv2.warpPerspective(image, M, (cols, rows))

cv2.imwrite("perspective_output.jpg", perspective_image)

cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformed Image", perspective_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
