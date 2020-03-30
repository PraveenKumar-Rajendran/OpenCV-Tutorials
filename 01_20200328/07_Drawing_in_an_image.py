import numpy as np
import cv2

img = cv2.imread('Ronaldo.jpg',cv2.IMREAD_UNCHANGED)

# LINE
# Parameters: image, start point, end point , color BGR Format , thickness
cv2.line(img,(0,0),(200,300),(255,255,255),50)

# RECTANGLE
# Parameters: image, top left point, bottom right point , color BGR Format , thickness
cv2.rectangle(img,(500,250),(1000,500),(0,0,255),15)

# CIRCLE
# Parameters: image, Center point, radius , color BGR Format , thickness ( -1 for filling in with the given colour )
cv2.circle(img,(447,63), 63, (0,255,0), -1)

# POLYGON
# Parameters: image, points , closing polygon flag (1st point to last point) , color , thickness
pts = np.array([[100,50],[200,300],[700,200],[500,100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0,255,255), 3)

font = cv2.FONT_HERSHEY_SIMPLEX
# Text Display
# Parameters: image, 'Text' , starting point , Font , Font size , Colour , Thickness ,
cv2.putText(img,'Praveen!',(10,500), font, 2.5, (200,255,155), 2, cv2.LINE_AA)
cv2.imshow('image',img)
cv2.waitKey(0) # Wait until any key is pressed
cv2.destroyAllWindows()