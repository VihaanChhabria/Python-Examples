#This code was made on the date of 10/30/2021
#Makesparts o the picture a random color
import cv2
import random
img = cv2.imread('C:\Vihaan\Python Examples\OpenCV Tutorial\Assets\Room.jpg', -1) #cv2.IMREAD_UNCHANGED can also be written as the number -1

#print(img.shape) #When printing out the shape of the picture it will show something like (720, 1280, 3). The first number means the height of the picture, the second number means the width of the picture, and the last number is the channels of the picture. The channel is the amount of values repesenting each pixel for example BGR.

#CHANGING PIXIL COLOR PART:
for i in range(100): #This will go through the x value of the picture (starting from the top) 100 times
    for j in range(img.shape[1]): #This will take the width of the pictures pixils
        #img[i][j] = [255, 255, 255] #This will make the pixils white
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)] #Makes the pixels random colors



#spider_man = img[414:472, 907:979]
#img[114:172, 607:679] = spider_man

cv2.imshow('thing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()