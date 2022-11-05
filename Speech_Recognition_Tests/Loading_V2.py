import pygame
from time import sleep

pygame.init()

img_1 = pygame.image.load('C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Loading_1.jpg')
img_2 = pygame.image.load('C:\Vihaan\Python Examples\Speech_Recognition_Tests\Speech_Recognition_Assets\Loading_2.jpg')

#display_width = 600
#display_height = 600

display_width, display_height = img_1.get_width(), img_1.get_height()

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Frame')

white = (255,255,255)

running = True

x =  0
y = 0

BIN_img = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    BIN_img = BIN_img * -1

    if BIN_img == -1:
        img = img_1
    else:
        img = img_2

    gameDisplay.fill(white)

    gameDisplay.blit(img, (x,y))
        
    pygame.display.update()

    sleep(0.5)

pygame.quit()
quit()