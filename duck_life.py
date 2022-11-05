import pyautogui
import time
counter = 70

time.sleep(5)
print(pyautogui.position())
while counter >= 0:
    pyautogui.click(x=1122, y=556)
    pyautogui.click(x=1122, y=556)
    time.sleep(0.5)

    pyautogui.click(x=1122, y=556)
    pyautogui.click(x=1122, y=556)
    time.sleep(0.5)

    pyautogui.click(x=1122, y=556)
    pyautogui.click(x=1122, y=556)
    time.sleep(0.5)

    pyautogui.click(x=1122, y=556)
    pyautogui.click(x=1122, y=556)
    time.sleep(1)

    pyautogui.click(x=1122, y=556)
    time.sleep(1)

    pyautogui.click(x=807, y=364)
    time.sleep(1)

    pyautogui.click(x=807, y=364)
    time.sleep(1)


    counter = counter - 1