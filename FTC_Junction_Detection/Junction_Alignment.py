import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Gets video.

colorDark = [219, 131, 44]
colorLight =[255, 176, 36]



def ColorAverage(image, num):
    channels = cv2.mean(image)
    observation = [channels[0], channels[1], channels[2]]

    img = np.zeros((480, 213, 3), np.uint8)
    img[:]=observation
    cv2.imshow("Avg{}".format(num), img)
    return observation

    
def ImgCropper(CropRange, num):
    cv2.imshow("cropped{}".format(num), CropRange)
    return CropRange

def ColorRange(color):
    red = False
    green = False
    blue = False
    if (color[0] >= colorDark[0]) and (color[0] <= colorLight[0]):
        red = True
    if (color[1] >= colorDark[1]) and (color[1] <= colorLight[1]):
        green = True
    if (color[2] >= colorLight[0]) and (color[2] <= colorDark[0]):
        blue = True

    if (red and green and blue):
        print("True")

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the variable frame.
    
    cv2.imshow("original", frame)
    
    frame1Color = ColorAverage(ImgCropper(frame[0:480, 0:213], 1), 1)
    frame2Color = ColorAverage(ImgCropper(frame[0:480, 213:426], 2), 2)
    frame3Color = ColorAverage(ImgCropper(frame[0:480, 426:640], 3), 3)

    ColorRange(frame2Color)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()