#Frame widgets are important for organizing the layout of your widgets in an application.
#An empty Frame widget is practically invisible. 
#Frames are best thought of as containers for other widgets.

import tkinter as tk

window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()

label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()

# Order of frames
frame_a.pack()
frame_b.pack()

window.mainloop()