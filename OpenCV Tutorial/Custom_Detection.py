import cv2

cap = cv2.VideoCapture(1) #Gets video.
count = 541

while True:
    ret, frame = cap.read() #This will take the dimensions of the camera with the varible frame.
    width = int(cap.get(3)) #This will get the width of the camera.
    height = int(cap.get(4)) #This will get the hieght of the camera.

    blur = int(cv2.Laplacian(frame, cv2.CV_64F).var())

    #img = cv2.putText(frame, str(blur), (10, height - 40), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 0, 255), 5, cv2.LINE_AA)

    if blur >= 20:
        cv2.imwrite('C:\Vihaan\Python Examples\OpenCV Tutorial\Assets\Custom_Haarcascade_V2\Rock_' + str(blur) + '_' + str(count) + '.jpg', frame)

        count = count + 1

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'): #This will close the program with the letter q.
        break
cap.release()
cv2.destroyAllWindows()