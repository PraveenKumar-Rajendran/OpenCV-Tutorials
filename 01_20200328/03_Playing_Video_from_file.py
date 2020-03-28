import numpy as np
import cv2

cap = cv2.VideoCapture('Playing_Video.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) #COLOR_BGR2RGB is the color space

    cv2.imshow('frame',gray)
    if cv2.waitKey(34) == -1 :  #34 millisecond is given because the original video used here is 30fps so 1000/30 gives 33.33. And waitkey() does not accepts float value. So 34 is given to stream it like the usual video
        pass
    else:
        break

#release the capture as always
cap.release()
#Closing the window after the stream is over
cv2.destroyAllWindows()