import numpy as np
import cv2

# Create a black image
img = np.zeros((512,512,3), np.uint8)

# Draw a diagonal green line with thickness of 10 px
img1 = cv2.line(img,(0,0),(511,511),(0,255,0),10)  # cv2.line(img, pt1, pt2, color[, thickness[, lineType[, shift]]])

# Display Line
cv2.imshow("Line",img1)

# wait for a sec
cv2.waitKey(1000)
cv2.destroyAllWindows()

# draw Rectangle
img2 = cv2.rectangle(img,(384,0),(511,511),(0,255,0),3)

# Display Rectangle
cv2.imshow("Rectangle",img2)

# wait for a sec
cv2.waitKey(1000)
cv2.destroyAllWindows()

# similarly for circle and other shapes
# enter co ordiante and radius is given for a circle
cv2.circle(img,(447,63), 63, (0,0,255), -1)

# Adding Text to Images
font = cv2.FONT_ITALIC
cv2.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv2.LINE_AA)

cv2.imshow("Text",img)

# wait for a sec
cv2.waitKey(1000)
cv2.destroyAllWindows()