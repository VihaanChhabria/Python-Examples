import cv2
import numpy as np

cap = cv2.VideoCapture(0) #Gets video.

while True:
    ret, frame = cap.read()
    channels = cv2.mean(frame)
    print(channels)

    # Swap blue and red values (making it RGB, not BGR)
    observation = np.array([(channels[0], channels[1], channels[2])])
    #observation = np.array([channels])

    #print(observation)

    height=512
    width=512
    blank_image = np.zeros((height,width,3), np.uint8)
    blank_image[:]=observation
    cv2.imshow('3 Channel Window', blank_image)
    cv2.imshow('Frame', frame)
    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()