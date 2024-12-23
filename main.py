import cv2
import numpy as np

# Load the image
img = cv2.imread('logo.png')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply thresholding to segment the object from the background
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Find contours in the thresholded image
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Create a mask with the same shape as the original image
mask = np.zeros(img.shape, dtype=np.uint8)

# Iterate through the contours and draw a filled polygon on the mask
for contour in contours:
    cv2.drawContours(mask, [contour], -1, (255, 255, 255), -1)

# Apply the mask to the original image
result = cv2.bitwise_and(img, mask)

# Save the output image
cv2.imwrite('output.png', result)
