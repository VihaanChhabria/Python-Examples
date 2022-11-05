import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

while running: 
    keys = key.get_pressed() 
    if keys[K_DOWN]: 
        print("DOWN") 