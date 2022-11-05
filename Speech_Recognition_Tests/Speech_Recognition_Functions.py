#Imports libraries
import speech_recognition as sr
import webbrowser
import numpy as np
import cv2
import pyautogui
import mouse
import os
import configparser

r = sr.Recognizer() 

mic = sr.Microphone() #Gets microphone permissions

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                print("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, "Speech_Recognition_Config.ini")
config = configparser.ConfigParser()
config.read(path_config_file)

global path
path = ConfigSectionMap("HomeFolder")['path']

def speech(): #Function for getting what speaker is saying
    try:
        with mic as source: #Initiates microphone
            r.adjust_for_ambient_noise(source) #Clears background noise
            audio = r.listen(source) #Starts listening

        return r.recognize_google(audio) #Returns what it heard
    except:
        return "Could Not Read Audio"

def image_finder(file, x, y): #Finds a image on a screen; needs what it is looking for, and the coordinates of it
    check = True

    while check:
        img = pyautogui.screenshot() #Takes a screenshot of screen

        img = cv2.cvtColor(np.array(img),
                            cv2.COLOR_RGB2BGR)

        cv2.imwrite(path + "image1.png", img) #Saves the screenshot

        img = cv2.imread(path + "image1.png", 0) #Reads the screenshot as a grayscale image
        find = cv2.imread(file, 0) #Reads the image provided in grayscale
        hs, ws = find.shape #Finds the shape of the image provided

        method = cv2.TM_CCOEFF_NORMED #Method for detecting the image provided

        result = cv2.matchTemplate(img, find, method)
        min_val_s, max_val_s, min_loc_s, max_loc_s = cv2.minMaxLoc(result) #Gets the location of the image
        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]: #Where the image gets the top left and bottom right of the image
            location = min_loc_s
        else:
            location = max_loc_s

        if location == (x, y): #Checks if the image detected is in the correct position
            check = False #Stops the code

def options_dir(): #What the speaker can do

    print()

    choice = speech() #Starts the recognition

    print(choice)

    return(choice)
    
def options(choice_option): #What the speaker can do
    if choice_option == "search": # Searches something on google
        s = speech()
        webbrowser.open(ConfigSectionMap("Links")['google'] + s.replace(" ", "+"))
    
    elif choice_option == "Minecraft":
        os.startfile(ConfigSectionMap("Applications")['minecraft']) #Opens minecraft launcher

        image_finder(path + 'Minecraft_Play.png', 834, 619) #Finds the play button

        mouse.move("834", "619") #Moves to the play button
        mouse.click() #Clicks the play button
        
    elif choice_option == "YouTube":
        webbrowser.open(ConfigSectionMap("Links")['youtube'])#Opens youtube
    
    elif choice_option == "onshape":
        webbrowser.open(ConfigSectionMap("Links")['onshape']) #Opens onshape

        image_finder(path + 'Cad_Sign_In.png', 597, 376) #Finds the login button

        mouse.move("834", "619") 
        mouse.click()

        mouse.move("597", "376") #Clicks the sign in button
        mouse.click()

    elif choice_option == "Netflix":
        webbrowser.open(ConfigSectionMap("Links")['netflix']) #Opens netflix

    elif choice_option == "Zoom":
        os.startfile(ConfigSectionMap("Applications")['zoom']) #Opens zoom

    elif choice_option == "Google meet":
        webbrowser.open(ConfigSectionMap("Links")['google_meet']) #opens google meet

    elif ((choice_option == "visual studio code") or (choice_option == "vs code")):
        os.startfile(ConfigSectionMap("Applications")['vs_code']) #Opens Visual Studio Code

    elif choice_option == "School":
        webbrowser.open(ConfigSectionMap("Links")['mail_school']) #Opens school gmail, school calender, google classroom, and the pvsd website
        webbrowser.open(ConfigSectionMap("Links")['classroom'])
        webbrowser.open(ConfigSectionMap("Links")['calendar'])
        webbrowser.open(ConfigSectionMap("Links")['pvsd'])

    elif choice_option == "science":
        webbrowser.open(ConfigSectionMap("Links")['mvp']) #Opens MVP sign in

        image_finder(path + "MVP_Sign_In.png", 645, 443) #Finds the sign in button

        mouse.move("708", "387") #Clicks on the password button
        mouse.click()

        mouse.move("730", "442") #Clicks on preset password
        mouse.click()

        mouse.move("645", "443") #Clicks on the sign in button
        mouse.click()

        image_finder(path + "Dashboard_Launch.png", 441, 696) #Finds the launch button

        mouse.move("491", "714") #Clicks on the launch button
        mouse.click()

        image_finder(path + "Edgenuity_Launch.png", 297, 484) #Finds the second launch button

        mouse.move("340", "494") #Clicks on the second launch button
        mouse.click()

    elif choice_option == "paint": #Opens paint
        os.startfile(ConfigSectionMap("Applications")['paint'])

    elif ((choice_option == "command prompt") or (choice_option == "CMD")): #Opens cmd
        os.startfile(ConfigSectionMap("Applications")['paint'])

    elif choice_option == "file explorer": #Opens file explorer
        os.startfile(ConfigSectionMap("Applications")['file_explorer'])

    elif choice_option == "Gmail": #Opens gmail
        webbrowser.open(ConfigSectionMap("Links")['mail_personal'])

    elif choice_option == "WhatsApp": #Opens whatsapp
        webbrowser.open(ConfigSectionMap("Links")['whatsapp'])

    elif choice_option == "calculator": #Opens calculator
        os.startfile(ConfigSectionMap("Applications")['calc'])

    else:
        return("Invalid Choice")
    