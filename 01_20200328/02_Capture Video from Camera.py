import numpy as np
import cv2

#0 & -1  works to select the default one.  1,2,3 etc for different devices
VideoCapture_device = 0
cap = cv2.VideoCapture(VideoCapture_device)

while(True):
    # Capture frame-by-frame , returns a boolean value. If frame is read correctly then True
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()