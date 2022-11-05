#This code was made on the date of 10/30/2021 - 10/31/2021
#Testing with cameras
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Gets video.

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the varible frame.
    width = int(cap.get(3)) #This will get the width of the camera.
    height = int(cap.get(4)) #This will get the hieght of the camera.

    image = np.zeros(frame.shape, np.uint8) #This will create a black screen in the dimensions of the camera.
    smaller_frame = cv2.resize(frame, (0,0), fx = 0.5 ,fy = 0.5) #This will shink the intire dimensions of the camera by half letting 4 cameras be shown.
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #This will paste the camera in the top left of the screen. This will rotate the camera too.
    image[height//2:, :width//2] = smaller_frame #This will paste the camera in the bottom left of the screen.
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180) #This will paste the camera in the top right of the screen. This will rotate the camera too.
    image[height//2:, width//2:] = smaller_frame #This will paste the camera in the bottom right of the screen.

    cv2.imshow('frame', image)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()