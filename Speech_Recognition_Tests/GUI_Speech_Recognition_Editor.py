import pygame
import configparser
import os
import sys

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

pygame.init()

path_current_directory = os.path.dirname(__file__)
path_config_file = os.path.join(path_current_directory, "Speech_Recognition_Config.ini")
config = configparser.ConfigParser()
config.read(path_config_file)

path = ConfigSectionMap("HomeFolder")['path']

frame_5 = pygame.image.load(path + ConfigSectionMap("Frames")['frame_5'])

exo = ConfigSectionMap("Fonts")['exo']

font = pygame.font.Font(path + exo, 25)

x, y = frame_5.get_width() * 0.5, frame_5.get_height() * 0.5

frame_5 = pygame.transform.scale(frame_5, (x, y))

gameDisplay = pygame.display.set_mode((x,y))
pygame.display.set_caption('Frame')

running = True

while running:
    for event in pygame.event.get(): #A key is pressed
        if event.type == pygame.QUIT: #Presses the X button
            running = False # Stops the loop    

    gameDisplay.blit(frame_5, (0, 0))

    text = font.render("hi", True, (255, 0, 0))

    textRect = text.get_rect()

    textRect.topleft = (72, 142)

    gameDisplay.blit(text, textRect)
        
    pygame.display.update()

pygame.quit()
sys.exit()