import tkinter as tk

window = tk.Tk() #Creates a window

###LABEL###

label = tk.Label(
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black",  # Set the background color to black
    width=10,
    height=10
)
label.pack() #Adds label into window

#width and height are measured in text units

#Color Names:
# "red"
# "orange"
# "yellow"
# "green"
# "blue"
# "purple"
# Any Hex Number ; https://www.rapidtables.com/convert/color/rgb-to-hex.html or https://htmlcolorcodes.com/

#fg = foreground, bk = background




###BUTTON###

def button_function():
    print("You Clicked The Button")

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
    command=button_function
)
button.pack() #Adds button into window




###ENTRY###

entry = tk.Entry(
    fg="yellow",
    bg="blue", 
    width=50
)
entry.pack()

entry.get() #Gets text in entry
entry.delete(0) #Deletes first letter in entry
entry.delete(0, 4) #Deletes first 4 letters in entry
entry.insert(0, "Python") #Adds text at start of entry




###TEXTBOX###

text_box = tk.Text()
text_box.pack()

text_box.get("1.0") # 1 of 1.0 means the first line, .0 of 1.0 means the first letter on the line 
text_box.get("1.0", "1.5") # May also do ranges
text_box.get("1.0", tk.END) #Gets all in the text box; example = 'Hello\nWorld\n'

text_box.delete("1.0") # Can delete letters
text_box.delete("1.0", "1.5") # May also do ranges
text_box.delete("1.0", tk.END) #Deletes everything

text_box.insert("1.0", "Hello") #Inserts 'Hello' on the first line first letter
text_box.insert("2.0", "\nWorld") #Inserts 'Hello' on the second line first letter
text_box.insert(tk.END, "Put me at the end!") #Puts text at the end of the textbox




window.mainloop() #Runs the event loop