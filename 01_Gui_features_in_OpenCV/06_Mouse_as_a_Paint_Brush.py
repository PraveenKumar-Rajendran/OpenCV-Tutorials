# import cv2
#
# events = [i for i in dir(cv2) if 'EVENT' in i]
#
# print (events)

import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK: # left Double click event
        cv2.circle(img,(x,y),100,(0,0,255),-1 )  # Draw a red circle, -1 for filling in the circle instaed of the line but we can specify the thickness of a line we want

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)

while(1):
    cv2.imshow('image',img)
    if cv2.waitKey(20) & 0xFF == ord('q'):  # 27 - ASCII value of 'q'
        break
cv2.destroyAllWindows()