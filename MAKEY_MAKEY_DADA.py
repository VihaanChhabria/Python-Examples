import keyboard  # using module keyboard
import playsound # Test commit
points = 0
while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('delete'):  # if key 'q' is pressed 
            print(points)
            quit()
            
        if keyboard.is_pressed('space'):
            points = points + 1
            playsound('AAA.wav')
            print(points)     


    except:
        break  # if user pressed a key other than the given key the loop will break
