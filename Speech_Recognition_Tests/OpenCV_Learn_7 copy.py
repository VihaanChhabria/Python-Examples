import numpy as np
import cv2
import pyautogui
import time
import mouse

check = True

while check:
    time.sleep(5)

    img = pyautogui.screenshot()

    img = cv2.cvtColor(np.array(img),
                        cv2.COLOR_RGB2BGR)

    cv2.imwrite("image1.png", img)

    img = cv2.imread("image1.png", 0)
    img = cv2.imread('C:\Vihaan\Python Examples\image1.png', 0) #Loads in main picture in gray scale
    spider = cv2.imread('C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Edgenuity_Launch.png', 0) #Loads picture of a spider in main picture in gray scale
    hs, ws = spider.shape #Finds the width and height of the spider
    print(hs)
    print(ws)

    method = cv2.TM_CCOEFF_NORMED

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

    print(max_loc_s)

    if location == (645, 443):
        check = False

#mouse.move("645", "443")
#mouse.click()

cv2.imshow('Match', final_img)
cv2.waitKey(0)
cv2.destroyAllWindows()