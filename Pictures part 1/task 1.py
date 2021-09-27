import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800,800))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (255, 255, 0)
PINK = (230, 50, 230)
RED = (240, 0, 0)

rect(screen, GRAY, (0, 0, 800, 800)) 
circle(screen, YELLOW, (400, 400), 200)
circle(screen, BLACK, (400, 400), 201, 1)

line(screen, BLACK, (300, 500), (500, 500), 40)

r1 = 40
r2 = 30
r3 = 15
L1 = 100
L2 = 80
sqrt = 2**0.5*0.5

circle(screen, RED, (300, 350), r1)
circle(screen, BLACK, (300, 350), r3)
circle(screen, BLACK, (300, 350), r1, 1)

circle(screen, RED, (500, 350), r2)
circle(screen, BLACK, (500, 350), r3)
circle(screen, BLACK, (500, 350), r2, 1)

polygon(screen, BLACK, [[208, 236], [364, 324],
                           [356, 338], [200, 246]])

polygon(screen, BLACK, [[440, 324], [600, 264],
                           [606, 280], [444, 342]])


pygame.display.update()
clock = pygame.time.Clock()
finished = True


while finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = False
    clock.tick(FPS)

pygame.quit()
