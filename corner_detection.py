import cv2
import numpy as np

img = cv2.imread('./assets/pyplay.png')
img = cv2.resize(img, (0,0), fx=.5, fy=.5)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


corners = cv2.goodFeaturesToTrack(grayscale, 100, .3, 10)
#source, number of corners, minimum quality, minimum euclidean distance
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel() #Flats the corner value
    cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

for i in range(len(corners)):
    for j in range(i +1, len(corners)):
        corner1 = tuple(corners[i].ravel())
        corner2 = tuple(corners[j].ravel())
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))
        cv2.line(img, corner1, corner2, (255, 0, 0), 1)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()