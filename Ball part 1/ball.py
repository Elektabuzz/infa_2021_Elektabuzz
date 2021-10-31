import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1000,700))

X = []
V_X = []
Y = []
V_Y = []
R = []
i = 0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

score = 0

def new_ball():
    '''draw new ball'''
    global x, y, r, v_x, v_y
    x = randint(100, 900)
    v_x = randint(-10, 10)
    v_y = randint(-10, 10)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

pygame.display.update()
clock = pygame.time.Clock()
procces = True

while procces:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            procces = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            Z = [0 for k in range(i)]
            for j in range (i):
                
                Z[j] = R[j] - ((event.pos[0]-X[j])**2+(event.pos[1]-Y[j])**2)**0.5 #


            for l in range (i):
                if Z[l] >= 0:
                    score += 1
                    print(score)
                    circle(screen, BLACK, (X[l], Y[l]), R[l])
                    X.pop(l)
                    Y.pop(l)
                    R.pop(l)
                    l -= 1
                    i -= 1
                    
    
    #процес создания шариков        
    new_ball()
    pygame.display.update()
    X.append(x)
    V_X.append(v_x)
    Y.append(y)
    V_Y.append(v_y)
    R.append(r)
    i += 1
    

pygame.quit()

#####Сделать скорости, сократить количество шариков до 2-4 (не прийдется запариваться), сделать вывод таблицы лучших игроков, ***сделать счет прямо в игре***, добавить другие мишени, задокументировать, сделать слои
