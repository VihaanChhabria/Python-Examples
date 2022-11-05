import cv2
import keyboard
import numpy as np

text = ""

while True:
    frame = np.zeros((512, 512, 3), dtype = "uint8") #This will take tahe dimensions of the camera with the varible frame.
    width = int(640) #This will get the width of the camera.
    height = int(480) #This will get the hieght of the camera.


    font = cv2.FONT_HERSHEY_COMPLEX
    a = keyboard.read_key()
    if a:
        if a == "backspace":
            text = text[:-1]
        else:
            text = text + a
            img = cv2.putText(frame, text, (10, height - 40), font, 2, (255, 0, 255), 5, cv2.LINE_AA) #(the picture it is going to draw on, the text, the bottom right of the text to put it on the picture, the font, how think the font is, the color, how big all of the text is, makes the text look better)

    cv2.imshow('frame', img)
    print(a)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cv2.destroyAllWindows()