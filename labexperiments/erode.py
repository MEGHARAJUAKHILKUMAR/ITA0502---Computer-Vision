import cv2
import numpy as np

image_path = r'C:\Users\akhil\OneDrive\Pictures\Screenshots\micky.png'


img = cv2.imread(image_path)

if img is None:
    print(f"❌ Error: Could not read image at path:\n{image_path}")
    print("Please check that the filename and extension (.png, .jpg, etc.) are correct!")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

kernel = np.ones((5, 5), np.uint8)

eroded_img = cv2.erode(gray, kernel, iterations=1)

cv2.imshow('Original Image', gray)
cv2.imshow('Eroded Image', eroded_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
