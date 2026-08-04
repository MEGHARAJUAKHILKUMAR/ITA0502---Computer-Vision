import cv2
import numpy as np

image = cv2.imread("mickey.jpg")

h, w = image.shape[:2]

src_pts = np.float32([
    [50, 50],
    [300, 50],
    [50, 300],
    [300, 300]
])

dst_pts = np.float32([
    [10, 100],
    [280, 50],
    [80, 300],
    [320, 280]
])

H, status = cv2.findHomography(src_pts, dst_pts)

output = cv2.warpPerspective(image, H, (w, h))

cv2.imwrite("homography_output.jpg", output)

cv2.imshow("Original Image", image)
cv2.imshow("Homography Transformed Image", output)

cv2.waitKey(0)
cv2.destroyAllWindows()
