#Uses os commands in python and opens websites
import os
import webbrowser

IP = "192.168.1.151"
URL = "https://www.google.com/"
choice = 0

while True:
    print("Go to CMD (1)")
    print("Go to PING (2)")
    print("Go to GOOGLE (3)")
    print("Go to CD (4)")
    print("Go to IPCONFIG (5)")
    print("Go to NOTEPAD (6)")
    choice = input("What Do you want to do? ")

    if choice == "1":
        os.system("cmd.exe")

    if choice == "2":
        print("Other IP (1)")
        print("192.168.1.151 (2)")
        IP_INPUT = input("Home or New IP? ")
        if IP_INPUT == "1":
            IP = input("What is the new IP? ")
            os.system("ping.exe " + IP)
        if IP_INPUT == "2":
            IP = "192.168.1.151"
            os.system("ping.exe " + IP)

    if choice == "3":
        print("Mail (1)")
        print("Other Websites (2)")
        GOOGLE = input("What Website? ")
        if GOOGLE == "1":
            webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")
        if GOOGLE == "2":
            URL = input("Whats your URL? ")
            webbrowser.open_new(URL)



    if choice == "5":
        os.system("ipconfig.exe")

    if choice == "6":
        os.system("notepad.exe")

    if choice == "4":
        print("c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts (1)")
        print("Other Path (2)")
        PATH_INPUT = input("What Path? ")
        if PATH_INPUT == "1":
            os.chdir("c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts")
            os.system("cmd.exe")
        if PATH_INPUT == "2":
            PATH = input("Whats your Path? ")
            os.chdir(PATH)  
            os.system("cmd.exe")


#os.system("cmd.exe")                                                   CMD

#os.system("ping.exe" + IP)                                               PING

#webbrowser.open_new("https://mail.google.com/mail/u/0/#inbox")           GMAIL

#os.system("ipconfig.exe")                                                 IPCONFIG

#os.system("notepad.exe")                                                NOTEPAD

#os.chdir(r"c:\Program Files (x86)\Microsoft Visual Studio\Shared\Python37_64\Scripts")                               NEED TO LEARN HOW TO CD STUFF

#look on desktop