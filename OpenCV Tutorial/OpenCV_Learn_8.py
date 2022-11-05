import numpy as np
import cv2

cap = cv2.VideoCapture(0) #Getting video
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') #The methords made to find the face.
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml') #the methords made to find the eye.

while True:
    ret, frame = cap.read() #Getting one of the frames of the video

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #making the frame gray because the function "detectMultiScale" only allows gray scaled images
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces: #Gets where the face is on the screen and the height and width of the face.
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 5) #draws a rectangle around the face
        roi_gray = gray[y:y+w, x:x+w] #Gets where the face is on the screen and the height and width of the face in gray scaled.
        roi_color = frame[y:y+h, x:x+w] #Gets where the face is on the screen and the height and width of the face.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5) #gets where the eyes are on the face
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 5) #Making a rectangle around the eyes
 
    cv2.imshow('frame', frame) #Displaying the frame

    if cv2.waitKey(1) == ord('q'): #Ends code with letter "q"
        break

cap.release()
cv2.destroyAllWindows()