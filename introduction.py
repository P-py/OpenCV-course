import cv2 #OpenCV

## Loading an image
# [variable] = cv2.imread([path], [mode])
"""
OpenCV can read images in many modes:
-1 -> Loads a color image.
0 -> Loads image in grayscale mode.
1 -> Loads image including alpha channel.
"""

img = cv2.imread('./assets/pyplay.png', 0)

## Displaying the image
# cv2.imshow([label], [variable]) - Displays
# cv2.waitKey(0) - Waits for a infinite time to a key
# cv2.destroyAllWindows() - Destroys the window
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Other modes
"""img2 = cv2.imread('./assets/pyplay.png', -1)
cv2.imshow('Image', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

img3 = cv2.imread('./assets/pyplay.png', 1)
cv2.imshow('Image', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

## Resizing an image
# [variable] = cv2.resize([image variable], ([size]))
img_resized = cv2.resize(img, (400, 400))
cv2.imshow('Image', img_resized)
cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to use float numbers for the resizing use:
# img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# You can change the fx and fy values to any floating or integer number.


## Rotating an image
img_rotate = cv2.rotate(img, cv2.cv2.ROTATE_180)
#There are another rotating options, just look at the docs.
cv2.imshow('Image rotated', img_rotate)
cv2.waitKey(0)
cv2.destroyAllWindows()

## Writing/saving an image
print("Saving the rotated image.")
cv2.imwrite('new_image.png', img_rotate)
