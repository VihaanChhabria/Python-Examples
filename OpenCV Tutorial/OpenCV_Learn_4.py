#This code was made on the date of 10/31/2021
#Testing with lines
import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Gets video.

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the varible frame.
    width = int(cap.get(3)) #This will get the width of the camera.
    height = int(cap.get(4)) #This will get the hieght of the camera.

    print(str(width) + "   " + str(height))

    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10) #When the program says frame it means the picture it is going to draw a line on. Whem it says 0,0 it means the line starts at 0,0. When it says (width, height)it means it ends at the maximun width of the frame and the maximun hieght of the image. When it says (255, 0, 0) it is the color of the line. Lastly when it says 10 its the size of the line
    img = cv2.line(frame, (0, height), (width, 0), (0, 255, 0), 10)
    img = cv2.rectangle(frame, (100, 100), (200, 200), (0, 0, 255), 10) #When the program says frame it means the picture it is going to draw a rectangle on. When it says (100, 100) that is where the top left of the rectangle starts. When it says (200, 200) it is where the bottom right of the rectangle ends. When it says (255, 0, 0) it is the color of the rectangle. Lastly where it says 10 it is the size of the lines but if it says -1 it means the rctangle is going to be filled it.
    img = cv2.circle(frame, (300, 300), 60, (0, 165, 255), 10) #When the program says frame it means the picture it is going to draw a line on. Whn the code says 60 it is the radios of the circle. When it says (0, 0, 0) it is the color. 10 is the size of the line.
    font = cv2.FONT_HERSHEY_COMPLEX
    img = cv2.putText(frame, 'This is very cool!', (10, height - 40), font, 2, (255, 0, 255), 5, cv2.LINE_AA) #(the picture it is going to draw on, the text, the bottom right of the text to put it on the picture, the font, how think the font is, the color, how big all of the text is, makes the text look better)

    cv2.imshow('frame', img)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()