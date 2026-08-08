import cv2

image = cv2.imread("C:\Users\akhil\OneDrive\Pictures\Screenshots\Screenshot 2026-07-11 114125.png")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 200)

cv2.imwrite("canny_output.png", edges)

cv2.imshow("Original Image", image)
cv2.imshow("Canny Edge Detection", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image outline detected successfully using the Canny function.")
