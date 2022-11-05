import mouse
import time
import keyboard

x = 0
y = 0

time.sleep(5)
while x < 5000:

    print("h")
    mouse.click('left')
    time.sleep(0.01)
    x = x + 1

#while y < 500:
#    while x < 745:
#        mouse.move(352+x, 182+y, absolute=True, duration=0.1)
#        mouse.click('left')
#        print(y)
#        x = x + 51
#    y = y + 24
#    x = 0
#    print("done")