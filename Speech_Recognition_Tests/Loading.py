#This code was made on the date of 10/31/2021
#Testing with lines
import cv2
import time

img_1 = cv2.imread('C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Loading_1.jpg', -1)
img_2 = cv2.imread('C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Loading_2.jpg', -1)

BIN_img = 1

while True:


    #font = cv2.FONT_HERSHEY_COMPLEX
    #img = cv2.putText(frame, 'This is very cool!', (10, height - 40), font, 2, (255, 0, 255), 5, cv2.LINE_AA) #(the picture it is going to draw on, the text, the bottom right of the text to put it on the picture, the font, how think the font is, the color, how big all of the text is, makes the text look better)

    BIN_img = BIN_img * -1

    if BIN_img == -1:
        img = img_1
    else:
        img = img_2

    cv2.imshow('frame', img)

    time.sleep(0.5)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cv2.destroyAllWindows()