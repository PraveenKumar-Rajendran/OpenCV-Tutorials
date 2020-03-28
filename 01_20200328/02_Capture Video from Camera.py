import numpy as np
import cv2

#0 & -1  works to select the default one.  1,2,3 etc for different devices
VideoCapture_device = 0
cap = cv2.VideoCapture(VideoCapture_device)

while(True):
    # Capture frame-by-frame , returns a boolean value. If frame is read correctly then True
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cv2.imshow('frame', gray)
    # Display the resulting frame
    #When no key is pressed the return value of the waitkey() is found to be -1
    #So using that to break the loop

    if  cv2.waitKey(1) == -1 :  # wait for millisecond per frame and if no key is pressed continue streaming, otherwise break the loop
        pass
    else:
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()