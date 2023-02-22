import os
import pyautogui
from time import sleep
os.startfile(r"C:\Users\vihaa\OneDrive\Desktop\Zoom.lnk")

MeetingButtonLoc = pyautogui.locateOnScreen(r'C:\Users\vihaa\Python-Examples\ZoomLauncherApp\ZoomMeetingButton.png')
sleep(2)

print(MeetingButtonLoc)