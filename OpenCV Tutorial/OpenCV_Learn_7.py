import numpy as np
import cv2

img = cv2.imread(r'C:\Users\vihaa\Python-Examples\OpenCV Tutorial\Assets\Room.jpg', 0) #Loads in main picture in gray scale
spider = cv2.imread(r'C:\Users\vihaa\Python-Examples\OpenCV Tutorial\Assets\spider.jpg', 0) #Loads picture of a spider in main picture in gray scale
head = cv2.imread(r'C:\Users\vihaa\Python-Examples\OpenCV Tutorial\Assets\head.jpg', 0) #Loads picture of a head in main picture in gray scale
hs, ws = spider.shape #Finds the width and height of the spider
hh, wh = head.shape #Finds the width and height of the head

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, #These are the methords of finding the images, some of them are bad some of them are good. We are testing them right now.
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods: #Going through the different methords one by one
    img2 = img.copy() #Making a copy of the main image

    result = cv2.matchTemplate(img2, spider, method) #Will search the main image for the spider
    min_val_s, max_val_s, min_loc_s, max_loc_s = cv2.minMaxLoc(result) #Will get the result of it
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #Where the image gets the top left and bottom right of the image
        location = min_loc_s
    else:
        location = max_loc_s

    final_img = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR) #Converts the image for the sqare to not be gray scaled

    bottom_right_s = (location[0] + ws, location[1] + hs)    
    cv2.rectangle(final_img, location, bottom_right_s, 255, 5) #Draws the rectangle




    result = cv2.matchTemplate(img2, head, method) #Will search the main image for the head
    min_val_h, max_val_h, min_loc_h, max_loc_h = cv2.minMaxLoc(result) #Will get the result of it
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #Where the image gets the top left and bottom right of the image
        location1 = min_loc_h
    else:
        location1 = max_loc_h

    bottom_right_h = (location1[0] + wh, location1[1] + hh)    
    cv2.rectangle(final_img, location1, bottom_right_h, 255, 5)#Draws the rectangle

    
    cv2.imshow('Match', final_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()