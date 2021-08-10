import numpy as np
import cv2
 
# Load an color image in grayscale
img = cv2.imread('pic.png',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
cv2.waitKey(10000) # Time in miliseconds
cv2.destroyAllWindows()