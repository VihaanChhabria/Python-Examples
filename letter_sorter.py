#print()
#word = input()
#letters = list(word)
#letters.sort()

#conjoined = "".join(letters)
#print(conjoined)
combined = ""

from pynput.keyboard import Key, Listener
  
def show(key):
  
    print(format(key))
    
    #print(combined + key)

    if key == Key.delete:
        # Stop listener
        return False

    if key == Key.backspace:
        # Stop listener
        return False
  
# Collect all event until released
with Listener(on_press = show) as listener:   
    
    listener.join()