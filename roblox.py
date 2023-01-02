import mouse
import time
import keyboard

x = 0
y = 0

time.sleep(5)
while x < 10000:

    print("h")
    mouse.click('left')
    time.sleep(0.01)
    x = x + 1
