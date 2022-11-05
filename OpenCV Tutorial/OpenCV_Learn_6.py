import cv2
import numpy as np

img = cv2.imread('C:\Vihaan\Python Examples\OpenCV Tutorial\Assets\chessboard.png') #Loading in image
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5) #makes image smaller
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Good features to track only allows gray

corners = cv2.goodFeaturesToTrack(gray, 100, 0.5, 10) #(image, how many corners there can be seen, the ableness to see the corners, how many pixil they can be apart to be seen)
corners = np.int0(corners) #making them into a int

for corner in corners:
    x, y = corner.ravel() #will flatten the corner arrays for example [[1, 1]] -> [1,1]
    cv2.circle(img, (x, y), 10, (0, 0, 255), -1) #putting a circle on the corner

cv2.imshow('frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()