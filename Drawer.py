#Draw things with your mouse
import pygame

pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Drawer")
clock = pygame.time.Clock()

loop = True
press = False
r = 0
b = 0
g = 0
while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
    
        mx, my = pygame.mouse.get_pos()
        keys = pygame.key.get_pressed()
        if pygame.mouse.get_pressed() == (1,0,0):
            pygame.draw.rect(screen, (r,b,g), (mx,my,10,10))
            pygame.display.update()

        if pygame.mouse.get_pressed() == (0,0,1):
            pygame.draw.rect(screen, (0,0,0), (mx,my,10,10))
            print("pygame.draw.rect(win, (255,128,0), (",mx,",", my,", width, height))")
            pygame.display.update()
        if keys[pygame.K_q]:
            r = r + 1
            print(r, ",", b, ",", g)
        if keys[pygame.K_w]:
            b = b + 1
            print(r, ",", b, ",", g)
        if keys[pygame.K_e]:
            g = g + 1
            print(r, ",", b, ",", g)
        if keys[pygame.K_a]:
            r = r - 1
            print(r, ",", b, ",", g)
        if keys[pygame.K_s]:
            b = b - 1
            print(r, ",", b, ",", g)
        if keys[pygame.K_d]:
            g = g - 1
            print(r, ",", b, ",", g)
pygame.quit()