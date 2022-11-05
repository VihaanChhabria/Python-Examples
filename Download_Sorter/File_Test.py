import os
import keyboard

while True:
    print(keyboard.read_key())
    if (keyboard.read_key() == "ctrl") and (keyboard.read_key() == "shift"):
        os.system("start cmd /K cd C:\\Vihaan\\Python\\Scripts" )
        break