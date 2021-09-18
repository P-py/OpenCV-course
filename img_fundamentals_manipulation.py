import cv2
import numpy as np

img = cv2.imread('./assets/pyplay.png', -1)
import random

## Image representation
print(img) # Output is a numpy array
print(type(img)) # <class 'numpy.ndarray'>
print(img.shape) # (1024, 1024, 4); - height, width and channels

# When you load a image with openCV its stored in a numpy array

# The standard color channels for OpenCV are BGR, not RGB

## Acessing pixel values
print(img[257][512:1024])

## Changing pixel colors
"""for i in range(100):
    for j in range(img.shape[1]):
        #(rows, columns, channels)
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
"""

"""cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

## Copying and pasting parts of the image
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
