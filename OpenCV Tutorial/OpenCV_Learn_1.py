#This Program will resize a picture then, rotate it clockwise. Lastly it will make the changes to the image into a new image.
#This code was made on the date of 10/30/2021
import cv2

img = cv2.imread('C:\Vihaan\Python Examples\OpenCV Tutorial\Assets\Room.jpg', -1) #cv2.IMREAD_UNCHANGED can also be written as the number -1
#img = cv2.resize(img, (500,500)) This would resize the picture ro the exact dimensions given
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5) #This will multiply the image's x and y lenghts by the number given making the picture not look weird
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) #This will flip the image clockwise by 90 degrees. The types of rotations are ROTATE_90_CLOCKWISE, ROTATE_180, and ROTATE_90_COUNTERCLOCKWISE
cv2.imwrite('C:\Vihaan\Python Examples\OpenCV Tutorial\Assets\Room1.jpg', img) #This will take all of the changes that have been made and make it into a new file
cv2.imshow('thing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()