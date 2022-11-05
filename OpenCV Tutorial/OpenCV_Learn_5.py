#This code was made on the date of 10/31/2021
#This code will see a rubix cubes's blue side.
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Gets video.

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the varible frame.
    width = int(cap.get(3)) #This will get the width of the camera.
    height = int(cap.get(4)) #This will get the hieght of the camera.

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Converts the video into bgr.
    lower_blue = np.array([90, 50, 50]) #Where the program starts seeing color
    upper_blue = np.array([130, 255, 255]) #Where the program does not see the color

    mask = cv2.inRange(hsv, lower_blue, upper_blue) #Impiments the ranges to the frame

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()