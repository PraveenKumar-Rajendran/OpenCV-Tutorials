import numpy as np
import cv2

# Load an color image in grayscale
img1 = cv2.imread(r'Audi.jpg',1)
img2 = cv2.imread(r'Audi.jpg',0)
img3 = cv2.imread(r'Audi.jpg',-1)
img4 = cv2.imread(r'Ronaldo.jpg',-1)


#print(img)   #printing out the array representation for the image, If the image is not loaded it returns None.

#Displaying the Colour version of the image (Alpha channel is ignored)
cv2.imshow('image_Colour',img1)
#Displaying the grayscale version of the image
cv2.imshow('image_Grayscale',img2)
#Displaying the unchanged version of the image
cv2.imshow('image_Unchanged',img3)
#Here comes Ronaldo, to finish it off
cv2.imshow('Ronaldo',img4)


#cv2.waitKey(0)     #given parameter specifies the milliseconds for the wait time, for 0 it waits until any keystroke
k = cv2.waitKey(0)  #waitKey() Returns the ascii value of the pressed key and waits for the specified time
print(k)
cv2.destroyAllWindows()  # closes all the windows

#To save back the processed images

cv2.imwrite('AudiGrey.png',img2)
