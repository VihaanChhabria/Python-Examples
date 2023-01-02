import cv2
import numpy as np
height=512
width=512
blank_image = np.zeros((height,width,3), np.uint8)
blank_image[:]=(0,124,255)
cv2.imshow('3 Channel Window', blank_image)
cv2.waitKey(0)
cv2.destroyAllWindows()