import cv2
import numpy as np
import pytesseract

file = r'C:\Users\vihaa\Python-Examples\AutoClicker\PyQt5Tests\37114352-de0cbece-2226-11e8-884b-95ada42a2865.jpg'
img = cv2.imread(file)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ekernel = np.ones((1,2),np.uint8)
eroded = cv2.erode(gray, ekernel, iterations = 1)
dkernel = np.ones((2,3),np.uint8)
dilated_once = cv2.dilate(eroded, dkernel, iterations = 1)
ekernel = np.ones((2,2),np.uint8)
dilated_twice = cv2.erode(dilated_once, ekernel, iterations = 1)
th, threshed = cv2.threshold(dilated_twice, 200, 255, cv2.THRESH_BINARY)
dkernel = np.ones((2,2),np.uint8)
threshed_dilated = cv2.dilate(threshed, dkernel, iterations = 1)
ekernel = np.ones((2,2),np.uint8)
threshed_eroded = cv2.erode(threshed_dilated, ekernel, iterations = 1)
text = pytesseract.image_to_string(threshed_eroded)
print(''.join(x for x in text if x.isdigit()))