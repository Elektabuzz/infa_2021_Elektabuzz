import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700,1000))

WHITE = (255, 255, 255)
MOON = (240, 240, 240)
BLACKK = (8, 8, 8)
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

def r(z):
    a = round(z)
    return a

def spirit(x, y, k):
    
    #Тело
    
    polygon(screen, GRAY_LIGHT, [[x+r(126*k), y+r(26*k)], [x+r(147*k), y+r(34*k)], [x+r(165*k), y+r(52*k)],
                                 [x+r(188*k), y+r(71*k)], [x+r(215*k), y+r(93*k)], [x+r(227*k), y+r(110*k)],
                                 [x+r(228*k), y+r(131*k)], [x+r(213*k), y+r(139*k)], [x+r(199*k), y+r(143*k)],
                                 [x+r(192*k), y+r(156*k)], [x+r(181*k), y+r(183*k)], [x+r(157*k), y+r(182*k)],
                                 [x+r(139*k), y+r(180*k)], [x+r(126*k), y+r(186*k)], [x+r(102*k), y+r(208*k)],
                                 [x+r(88*k), y+r(208*k)], [x+r(72*k), y+r(187*k)], [x+r(44*k), y+r(170*k)],
                                 [x+r(5*k), y+r(176*k)], [x+r(17*k), y+r(157*k)], [x+r(23*k), y+r(139*k)],
                                 [x+r(34*k), y+r(123*k)], [x+r(45*k), y+r(100*k)], [x+r(56*k), y+r(81*k)],
                                 [x+r(62*k), y+r(50*k)]])
    
    circle(screen, GRAY_LIGHT, (x+r(76*k), y+r(54*k)), r(15*k))
    circle(screen, GRAY_LIGHT, (x+r(123*k), y+r(40*k)), r(15*k))

    #Голова
    circle(screen, GRAY_LIGHT, (x+r(90*k), y+r(30*k)), r(30*k))
    circle(screen, LIGHT_BLUE, (x+r(75*k), y+r(32*k)), r(8*k))
    circle(screen, LIGHT_BLUE, (x+r(105*k), y+r(27*k)), r(8*k))
    circle(screen, BLACK, (x+r(73*k), y+r(32*k)), r(2*k))
    circle(screen, BLACK, (x+r(102*k), y+r(27*k)), r(2*k))
    line(screen, WHITE, (x+r(74*k), y+r(30*k)), (x+r(77*k), y+r(29*k)), r(2*k))
    line(screen, WHITE, (x+r(103*k), y+r(25*k)), (x+r(106*k), y+r(24*k)), r(2*k))
    

def house(x, y, k):
    rect(screen, WOOD, (x+r(40*k), y+r(150*k), r(320*k), r(450*k)))

    #Крыша
    rect(screen, PIPE, (x+r(250*k), y+r(50*k), r(15*k), r(60*k)))
    polygon(screen, BLACK, [[x+0, y+r(160*k)], [x+r(60*k), y+r(105*k)], [x+r(345*k), y+r(105*k)], [x+r(420*k), y+r(160*k)]])
    rect(screen, PIPE, (x+r(130*k), y+r(40*k), r(25*k), r(110*k)))
    rect(screen, PIPE, (x+r(70*k), y+r(50*k), r(15*k), r(85*k)))
    rect(screen, PIPE, (x+r(300*k), y+r(20*k), r(10*k), r(130*k)))

    #Фурнитура
    for i  in range (5):
        rect(screen, WALL, (x+r((65+60*i)*k), y+r(161*k), r(35*k), r(190*k)))
    
    rect(screen, PIP, (x+0, y+r(370*k), r(410*k), r(50*k)))
    rect(screen, PIP, (x+r(25*k), y+r(295*k), r(350*k), r(25*k)))
    rect(screen, PIP, (x+r(18*k), y+r(320*k), r(7*k), r(50*k)))
    rect(screen, PIP, (x+r(375*k), y+r(320*k), r(7*k), r(50*k)))
    for i in range (4):
        rect(screen, PIP, (x+r((60+80*i)*k), y+r(320*k), r(15*k), r(50*k)))

    rect(screen, WIN, (x+r(85*k), y+r(470*k), r(60*k), r(100*k)))
    rect(screen, WIN, (x+r(175*k), y+r(470*k), r(60*k), r(100*k)))
    rect(screen, YELLOW, (x+r(265*k), y+r(470*k), r(60*k), r(100*k)))



#Фон
rect(screen, BLACKK, (0, 420, 700, 580))
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
house(0, 420, 0.7)
house(250, 300, 0.5)
house(500, 300, 0.3)

#spirit
spirit(400, 600, 1.5)
spirit(300, 540, 0.7)
spirit(50, 340, 0.4)
spirit(600, 420, 0.3)


clock = pygame.time.Clock()
pygame.display.update()
finish = True

while finish:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finish = False

pygame.quit()

