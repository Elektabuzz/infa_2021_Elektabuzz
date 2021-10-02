import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700,1000))

WHITE = (255, 255, 255)
MOON = (240, 240, 240)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
GRAY_LIGHT = (179, 179, 179)
LIGHT_BLUE = (135, 205, 222)
GREEN = (0, 200, 64)
YELLOW = (212, 180, 0)
PINK = (230, 50, 230)
RED = (240, 0, 0)
WOOD = (43, 34, 0)
PIPE = (32, 32, 32)
PIP = (30, 30, 30)
WALL = (72, 62, 55)
WIN = (43, 17, 0)
GRAYS = (90, 90, 90)

def spirit(x,y):
    
    #Тело
    polygon(screen, GRAY_LIGHT, [[x+126, y+26], [x+147, y+34], [x+165, y+52],
                                 [x+188, y+71], [x+215, y+93], [x+227, y+110],
                                 [x+228, y+131], [x+213, y+139], [x+199, y+143],
                                 [x+192, y+156], [x+181, y+183], [x+157, y+182],
                                 [x+139, y+180], [x+126, y+186], [x+102, y+208],
                                 [x+88, y+208], [x+72, y+187], [x+44, y+170],
                                 [x+5, y+176], [x+17, y+157], [x+23, y+139],
                                 [x+34, y+123], [x+45, y+100], [x+56, y+81],
                                 [x+62, y+50]])
    circle(screen, GRAY_LIGHT, (x+76, y+54), 15)
    circle(screen, GRAY_LIGHT, (x+123, y+40), 15)

    #Голова
    circle(screen, GRAY_LIGHT, (x+90, y+30), 30)
    circle(screen, LIGHT_BLUE, (x+75, y+32), 8)
    circle(screen, LIGHT_BLUE, (x+105, y+27), 8)
    circle(screen, BLACK, (x+73, y+32), 2)
    circle(screen, BLACK, (x+102, y+27), 2)
    line(screen, WHITE, (x+74, y+30), (x+77, y+29), 2)
    line(screen, WHITE, (x+103, y+25), (x+106, y+24), 2)
    

def house(x,y):
    rect(screen, WOOD, (x+40, y+150, 320, 450))

    #Крыша
    rect(screen, PIPE, (x+250, y+50, 15, 60))
    polygon(screen, BLACK, [[x+0, y+160], [x+60, y+105], [x+345, y+105], [x+420, y+160]])
    rect(screen, PIPE, (x+130, y+40, 25, 110))
    rect(screen, PIPE, (x+70, y+50, 15, 85))
    rect(screen, PIPE, (x+300, y+20, 10, 130))

    #Фурнитура
    for i  in range (5):
        rect(screen, WALL, (x+65+60*i, y+161, 35, 190))
    
    rect(screen, PIP, (x+0, y+370, 410, 50))
    rect(screen, PIP, (x+25, y+295, 350, 25))
    rect(screen, PIP, (x+18, y+320, 7, 50))
    rect(screen, PIP, (x+375, y+320, 7, 50))
    for i in range (4):
        rect(screen, PIP, (x+60+80*i, y+320, 15, 50))

    rect(screen, WIN, (x+85, y+470, 60, 100))
    rect(screen, WIN, (x+175, y+470, 60, 100))
    rect(screen, YELLOW, (x+265, y+470, 60, 100))



#Фон
rect(screen, BLACK, (0, 420, 700, 580))
rect(screen, GRAY, (0, 0, 700, 420))

#Луна
circle(screen, MOON, (600, 90), 80)

#Облака
ellipse(screen, PIP, (200, 300, 400, 80))
ellipse(screen, GRAYS, (120, 140, 250, 40))
ellipse(screen, GRAYS, (410, 120, 210, 50))
ellipse(screen, GRAYS, (20, 30, 340, 50))
ellipse(screen, GRAYS, (550, 260, 300, 40))

#House
house(0, 200)

#spirit
spirit(400, 600)


clock = pygame.time.Clock()
pygame.display.update()
finish = True

while finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False

pygame.quit()
