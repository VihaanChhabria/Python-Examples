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

    green_lower = (49,70,71)
    green_upper = (102, 255, 255)

    lower = np.array([green_lower]) #Where the program starts seeing color
    upper = np.array([green_upper]) #Where the program does not see the color

    mask = cv2.inRange(hsv, lower, upper) #Impiments the ranges to the frame

    kernel = np.ones((8,8),np.uint8)

    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    contours, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    output = cv2.drawContours(result, contours, -1, (0, 0, 255), 3)

    cv2.imshow('frame', result)
    cv2.imshow('mask', mask)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()