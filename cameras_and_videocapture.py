import cv2
import numpy as np

## Displaying video capture devices
capture = cv2.VideoCapture(0)
# The 0 stands for the video index of the devices
# You can also load videos, just change the index for the path

"""while True:
    ret, frame = capture.read()
    # Returns the frame and ret, a boolean condition to check if the video works.
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
capture.release()
cv2.destroyAllWindows()"""

## Mirroring video multiple times
capture = cv2.VideoCapture(0)


while True:
    ret, frame = capture.read()
    width = int(capture.get(3)) #Gets the width property of the frame/capture
    height = int(capture.get(4))

    image = np.zeros(frame.shape, np.uint8) #Empty black frame
    #uint8 = unasigned integer 8bits
    smaller_frame = cv2.resize(frame, (0,0), fx=.5, fy=.5)

    #Puts the smaller frame into the 1/4 of the canvas
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #Top Left
    image[height//2:, :width//2] = smaller_frame #Bottom Left
    image[:height//2, width//2:] = smaller_frame #Top Right
    image[height//2:, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #Bottom Right

    cv2.imshow('Frame', image)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()