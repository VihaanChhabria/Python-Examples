import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

run = True
count = 0

top, middle_right, bottom_right, bottom_left, middle_left = (146, 0),(291, 106),(236, 277),(56 , 277),(0, 106)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))  # Fills the screen with black

    pygame.draw.circle(win, (255,0,0), (400, 400), 5)

    pygame.draw.polygon(win,(0, 0, 255),(top, middle_right, bottom_right, bottom_left, middle_left))
    
    count = count + 1

    pygame.time.delay(100)

    pygame.display.update()
pygame.quit()