import pygame
import random
import time
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

width = 40
height = 40
vel = 5


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    time.sleep(2)

    x = random.randint(0, 500)
    y = random.randint(0, 500)

    xm,ym = pygame.mouse.get_pos()
    if xm and ym == x and y:
        pygame.quit()
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
pygame.quit()