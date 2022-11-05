#Imports
import sys
import pygame
import threading
from Speech_Recognition_Functions import *
import configparser

#Functions
def speech_background():
    global s
    s = ''
    while True:
        while mic_BIN == -1:
            pass
        if not running:
            sys.exit()
        s = speech() #Sees what speaker is saying

        print(s) #Prints what what speaker is saying

        if s == "my dude": #If the speaker says "my dude" (name of code)
            print("Recognized")

            s = options_dir() #Starts bringing up options
            options(s)

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

#Initialization
pygame.init()

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, "Speech_Recognition_Config.ini")
config = configparser.ConfigParser()
config.read(path_config_file)

path = ConfigSectionMap("HomeFolder")['path']

#frame_1 = pygame.image.load(r'C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Frame_1_V2.jpg')
frame_1 = pygame.image.load(path + ConfigSectionMap("Frames")['frame_1'])
frame_2 = pygame.image.load(path + ConfigSectionMap("Frames")['frame_2'])
frame_3 = pygame.image.load(path + ConfigSectionMap("Frames")['frame_3'])
frame_4 = pygame.image.load(path + ConfigSectionMap("Frames")['frame_4'])

microphone_on = pygame.image.load(path + ConfigSectionMap("Images")['microphone-on'])
microphone_off = pygame.image.load(path + ConfigSectionMap("Images")['microphone-off'])

mic_type = microphone_on

mic_BIN = 1

frames = [frame_1, frame_2, frame_3, frame_4]

frame_counter = 1

frame = frame_1

frame_scale_count = 0

x, y = frame.get_width() * 0.5, frame.get_height() * 0.5

while frame_scale_count < len(frames):
    frames[frame_scale_count] = pygame.transform.scale(frames[frame_scale_count], (x, y))
    frame_scale_count = frame_scale_count + 1

gameDisplay = pygame.display.set_mode((x,y))
pygame.display.set_caption('Frame')

left = pygame.Rect(46, 423.5, 120, 120)
right = pygame.Rect(285, 423.5, 120, 120)

mic_button = pygame.Rect(195, 439, 73, 73)

global running
running = True

path = ConfigSectionMap("HomeFolder")['path']
exo = ConfigSectionMap("Fonts")['exo']


font = pygame.font.Font(path + exo, 25)

speech_background_thread = threading.Thread(target = speech_background)
speech_background_thread.start()

#Loop
while running:
    for event in pygame.event.get(): #A key is pressed
        if event.type == pygame.QUIT: #Presses the X button
            running = False # Stops the loop

        if event.type == pygame.MOUSEBUTTONDOWN: #Left mouse button pressed
            mouse_pos = pygame.mouse.get_pos() #Gets mouse position
            if right.collidepoint(mouse_pos): #Sees if the mouse is over the right arrow
                frame_counter = frame_counter + 1 # Goes to the next slide

                if frame_counter > len(frames): #Stops the user from going over the limit
                    frame_counter = len(frames)

            if left.collidepoint(mouse_pos): #Sees if the mouse is over the right arrow
                frame_counter = frame_counter - 1 #Moves back on slide

                if frame_counter < 1: #Stops the user from going over the limit
                    frame_counter = 1

            if mic_button.collidepoint(mouse_pos):
                mic_BIN = mic_BIN * -1

    
    frame = frames[frame_counter - 1] #Moves the slide

    if mic_BIN == 1:
        mic_type = microphone_on

    else:
        mic_type = microphone_off

    gameDisplay.blit(frame, (0, 0))

    gameDisplay.blit(mic_type, (195, 439))

    text = font.render(s, True, (255, 209, 140))

    textRect = text.get_rect()
 
    textRect.bottomleft = (86, 377)

    gameDisplay.blit(text, textRect)
        
    pygame.display.update()

pygame.quit()
sys.exit()