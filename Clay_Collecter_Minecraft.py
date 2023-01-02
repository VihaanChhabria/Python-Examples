import keyboard
import mouse
import time

check = -1

time.sleep(5)

while True:
    if keyboard.is_pressed('ctrl'):
        check = check * -1
    while check == -1:
        if keyboard.is_pressed('ctrl'):
            check = check * -1
        keyboard.press_and_release("9")
        time.sleep(0.15)
        mouse.click("right")
        time.sleep(0.15)
        keyboard.press_and_release("8")
        time.sleep(0.15)
        mouse.press("left")
        time.sleep(0.3)
        mouse.release("left")
        time.sleep(0.15)