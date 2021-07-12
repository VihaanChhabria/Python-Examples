import random
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("hangman")
vel = 5

xH = 40
yH = 50
widthH = 40
heightH = 60

xS = 50
yS = 110
widthS = 20
heightS = 100

xA1 = 35
yA1 = 125
widthA1 = 15
heightA1 = 70

xA2 = 70
yA2 = 125
widthA2 = 15
heightA2 = 70

xL1 = 70
yL1 = 200
widthL1 = 15
heightL1 = 70

xL2 = 35
yL2 = 200
widthL2 = 15
heightL2 = 70

x = 50
y = 50
width = 40
height = 60
vel = 5
a = ["rction" , "hn", "schl", "hll", "ppr", "tn", "flwr", "mgntc", "ctps"]
b = (random.choice(a))
counter = 0
LivesLeft = 3
run = True

while counter < 3 :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    print("Random Word",b)
    c = input("type in the missing vowels(in lower case) ")

    if ((c == "eaio") or (c == "e") or (c == "oo") or (c == "i") or (c == "ae") or (c == "e") or (c == "oe") or (c == "aei") or (c =="oou")):
        print("correct")
        b = (random.choice(a))
    else :
        counter = counter + 1
        LivesLeft = LivesLeft - counter
        print("Lives left",LivesLeft)
    win.fill((0,0,0))

pygame.draw.rect(win, (255,0,0), (xH, yH, widthH, heightH))   
pygame.draw.rect(win, (0,225,0), (xS, yS, widthS, heightS))   
pygame.draw.rect(win, (0,0,255), (xA1, yA1, widthA1, heightA1))
pygame.draw.rect(win, (0,0,255), (xA2, yA2, widthA2, heightA2))
pygame.draw.rect(win, (225,0,0), (xL1, yL1, widthL1, heightL1))
pygame.draw.rect(win, (225,0,0), (xL2, yL2, widthL2, heightL2))
pygame.draw.rect(win, (225,225,255), (250, 1, 15, 500))
pygame.draw.rect(win, (225,225,255), (400, 1, 15, 50))
pygame.display.update()