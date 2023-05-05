import pyautogui
import keyboard
import time
import threading   

def click(): 
    while clickingAllowence:
        time.sleep(0.1)   
        print("clicking")
        pyautogui.click(button='right')

def move():
    while clickingAllowence:
        pyautogui.keyDown('a')

        time.sleep(0.75)

        pyautogui.keyUp('a')

        pyautogui.keyDown('d')

        time.sleep(0.75)

        pyautogui.keyUp('d')

def main():
    global clickingAllowence
    clickingAllowence = True

    c = threading.Thread(target=click, args=[])
    c.start()

    #m = threading.Thread(target=move, args=[])
    #m.start()

    while clickingAllowence:
        if keyboard.is_pressed('`'):
            clickingAllowence = False
            c.join()
            print("done")
            #m.join()

time.sleep(10)

main()