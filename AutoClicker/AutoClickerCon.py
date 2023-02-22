import pyautogui
import keyboard
import time
repeat = True

initialTime = 3
timeInterval = 3
holdInterval = 3


keyboardMouse = "Keyboard"
keyboardButton = "a"


mouseWheel = True
mouseWheelDis = "10"

mouseSide = 'right'

time.sleep(initialTime)

while repeat:
    if ((keyboard.is_pressed(99)) and (keyboard.is_pressed('ctrl')) and (keyboard.is_pressed('alt'))):
        repeat = False

    if keyboardMouse == "Keyboard":
        keyboard.press(keyboardButton)
        time.sleep(holdInterval)
        keyboard.release(keyboardButton)
    else:
        if mouseWheel:
            pyautogui.scroll(mouseWheelDis)
        else:
            pyautogui.mouseDown(button=mouseSide)
            time.sleep(holdInterval)
            pyautogui.mouseUp(button=mouseSide)


    time.sleep(timeInterval)