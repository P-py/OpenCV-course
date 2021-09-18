import cv2
import numpy as np

# It's important that the template image size is similar to the base image size.

base = cv2.imread('./assets/football.jpg', 0)
template = cv2.imread('./assets/ball2.png', 0)
# Transforming into grayscale is essential

height, width = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# Methos to template matching

"""cv2.imshow('Base', base)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

for method in methods:
    print(method)
    base_copy = base.copy()
    # A copy is necessary for each method to not draw on the same image
    result = cv2.matchTemplate(base_copy, template, method)
    min_value, max_value, min_location, max_location = cv2.minMaxLoc(result)
    # SQDIFF - Min value
    # Others - Max value
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_location
    else:
        location = max_location
    
    bottom_right = (location[0] + width, location[1] + height)
    #Defining the other point for the rectangle
    cv2.rectangle(base_copy, location, bottom_right, 255, 3)
    base_copy = cv2.resize(base_copy, (0, 0), fx=.5, fy=.5)
    cv2.imshow(f'{method}', base_copy)
    cv2.waitKey(0)
    cv2.destroyAllWindows()