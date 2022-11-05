import pygame
import threading

ball_count = 2

global d
d = {}
for x in range(1, ball_count + 1):
    d["string{0}".format(x)] = False

run = True

def ball(vx, vy, run, t, ball_num):
    x, y = 250, 250
    while run:                     
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.time.delay(t)
        x, y = vx + x, vy + y
        w, h = win.get_width(), win.get_height()

        if y <= 0:
            vy = abs(vy)
        elif y >= h:
            vy = vy * -1
        if x <= 0:
            vx = abs(vx)
        elif x >= w:
            vx = vx * -1

        win.fill((0,0,0))
        pygame.draw.circle(win, (255, 0, 0), (x, y), 25, 0)

        d["string" + str(ball_num)] = True
        while d["string" + str(ball_num)]:
            pass
        #pygame.display.update()

def update_check():
    while run:
        test_val = list(d.values())[0]

        for ele in d:
            if d[ele] != test_val:
                res = False
                pygame.display.update()
                for ele_c in d:
                    d[ele_c] = False

pygame.init()

win = pygame.display.set_mode((700,700), pygame.RESIZABLE)
pygame.display.set_caption("First Game")



#x, y = 250, 250 #Where the ball is

#vx, vy = 10, 10 # Velocity of the ball (direction and speed)



ball_thread_1 = threading.Thread(target = ball, args=(1, 5, run, 0, 1))
ball_thread_2 = threading.Thread(target = ball, args=(1, 2, run, 0, 2))
ball_thread_1.start()
ball_thread_2.start()

while run:                     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.time.delay(25)
    #pygame.display.update()
        
pygame.quit()


