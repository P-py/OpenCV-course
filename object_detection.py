import cv2
import numpy as np

# It's important that the template image size is similar to the base image size.

base = cv2.imread('./assets/launching.jpg', 0)
falcon9_template = cv2.imread('./assets/falcon9.png', 0)
# Transforming into grayscale is essential

height, width = falcon9_template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# Methos to template matching

for method in methods:
    base_copy = base.copy()
    # A copy is necessary for each method to not draw on the same image
    result = cv2.matchTemplate(base_copy, falcon9_template, method)
    