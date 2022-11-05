import pygame

pygame.init()


win = pygame.display.set_mode((500,500)) #pygame.RESIZABLE
pygame.display.set_caption("First Game")

run = True
count = 50

win_x, win_y = win.get_width(), win.get_height()

neg_or_pos = -1

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))  # Fills the screen with black
    pygame.draw.circle(win, (255, 0, 0), (250, 250), count, 0)
    
    count = count + neg_or_pos

    if count == 10:
        neg_or_pos = +1
    if count == 50:
        neg_or_pos = -1

    pygame.time.delay(50)

    pygame.display.update()
        
pygame.quit()