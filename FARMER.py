#In Minecraft it will farm for you
import pyautogui
import time
import mouse

time.sleep(5)


def ROW_FORWARDS():
    counter = 0
    while counter < 9:
        mouse.click('left')
        time.sleep(0.5)
        mouse.click('right')
        pyautogui.keyDown('w')
        time.sleep(0.15)
        pyautogui.keyUp('w')
        counter = counter + 1

def ROW_BACKWARDS():
    counter = 0
    while counter < 9:
        mouse.click('left')
        time.sleep(0.5)
        mouse.click('right')
        pyautogui.keyDown('s')
        time.sleep(0.15)
        pyautogui.keyUp('s')
        counter = counter + 1

ROW_FORWARDS()

pyautogui.keyDown('a')
time.sleep(0.15)
pyautogui.keyUp('a')

ROW_BACKWARDS()

pyautogui.keyDown('a')
time.sleep(0.15)
pyautogui.keyUp('a')

ROW_FORWARDS()

pyautogui.keyDown('a')
time.sleep(0.15)
pyautogui.keyUp('a')

ROW_BACKWARDS()

pyautogui.keyDown('a')
time.sleep(0.15)
pyautogui.keyUp('a')

ROW_FORWARDS()