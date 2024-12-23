Description
The script reads an image file (logo.png), converts it to grayscale, applies thresholding to create a binary image, 
detects the contours of the object, and then creates a mask to extract the object from the background. The final result is saved as an output image (output.png).

Key Steps in the Code:

>> Loading the Image: The image (logo.png) is read using OpenCV's cv2.imread() function.
>> Converting to Grayscale: The image is converted to grayscale using cv2.cvtColor() to simplify further processing.
>> Thresholding: A binary threshold is applied using Otsu's method (cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU) to segment the object from the background.
>> Finding Contours: Contours are detected in the thresholded image using cv2.findContours().
>> Creating a Mask: A mask with the same dimensions as the original image is created, and filled polygons are drawn on it based on the detected contours.
>> Applying the Mask: The mask is applied to the original image using cv2.bitwise_and() to extract the object.
>> Saving the Output: The resulting image is saved as output.png.

Requirements
>> Python 3.x
>> OpenCV (cv2): pip install opencv-python
>> NumPy: pip install numpy

Usage
>> Place the image (logo.png) in the same directory as the script.
>> Run the Python script.
>> The script will generate an output image (output.png) with the object segmented from the background.
