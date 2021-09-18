import cv2
import numpy as np

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()
    width = int(capture.get(3))
    height = int(capture.get(4))

    # The coords system works starting by 0,0 at the left top

    ## Drawing lines
    img = cv2.line(frame, (0,0), (width, height), (0, 0, 255), 10)
    #[variable] = cv2.line([source], [starting position], [ending], [color], [thickness])
    img = cv2.line(img, (0, height), (width, 0), (255, 0, 0), 10)

    ## Drawing rectangles
    img = cv2.rectangle(img, (width//2 - 100, height//2 - 100), (width//2 + 100, height//2 + 100), (0, 255, 0), 3)
    #[variable] = cv2.rectangle([source], [vertex1], [vertex2], [color], [thickness])
    # If you want to fill the rectangle just change the thickness to -1

    ## Drawing circles
    img = cv2.circle(img, (width//2, height//2), 50, (0, 0, 0), 3)
    #[variable] = cv2.circle([source], [center of the circle], [radius], [color], [thickness or fill])

    ## Drawing text
    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'Pedro is nice!', (0, 25), font, 1, (255, 255, 255), 3, cv2.LINE_AA)
    #[variable] = cv2.putText([source], [text], [bottom left corner], [font], [fontScale], [color], [thickness], [line type])

    cv2.imshow('Frame', img)
    
    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()