import customtkinter
from functools import partial

customtkinter.set_appearance_mode("dark") #Possible: dark, light, System
customtkinter.set_default_color_theme("green") #For checkboxes, borders... ; Possible: blue, dark-blue, green

root = customtkinter.CTk() #Creates Window
root.geometry("500x350") #X and Y length for window size

def login(username, password):
    print(username.get())
    print(password.get())

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx = 60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Login System", font=("Roboto", 24))
label.pack(pady=12, padx = 10)

entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx = 10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx = 10)

button = customtkinter.CTkButton(master=frame, text="Login", command=partial(login, entry1, entry2))
button.pack(pady=12, padx = 10)

checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx = 10)

root.mainloop()