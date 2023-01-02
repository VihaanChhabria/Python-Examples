import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Gets video.

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the variable frame.
    
    cv2.imshow("original", frame)
    
    cropped_image1 = frame[0:480, 0:213]
    cv2.imshow("cropped1", cropped_image1)


    cropped_image2 = frame[0:480, 213:426]
    cv2.imshow("cropped2", cropped_image2)


    cropped_image3= frame[0:480, 426:640]
    cv2.imshow("cropped3", cropped_image3)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()