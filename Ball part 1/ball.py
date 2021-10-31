import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000,700))

X = []
V_X = []
Y = []
V_Y = []
R = []
COLOR = []
t = 1
score = 0
u=0

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

file = open('score.txt', 'a')


def new_ball():
    '''draw new ball'''
    global x, y, r, v_x, v_y, color, i
    x = randint(100, 900)
    v_x = randint(-7, 7)
    v_y = randint(-7, 7)
    y = randint(100, 600)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    pygame.display.update()
    X.append(x)
    V_X.append(v_x)
    Y.append(y)
    V_Y.append(v_y)
    R.append(r)
    COLOR.append(color)
    
    
def move_balls():
    for j in range (k):
        circle(screen, BLACK, (X[j], Y[j]), R[j])
        if X[j]-R[j] <= 0:
            V_X[j] = -V_X[j]
            X[j] = X[j]+1
        elif X[j] + R[j] >= 1000:
            V_X[j] = -V_X[j]
            X[j] = X[j]-1
        elif Y[j]- R[j] <= 0:
            V_Y[j] = -V_Y[j]
            Y[j] = Y[j]+1
        elif Y[j]+R[j] >= 700:
            V_Y[j] = -V_Y[j]
            Y[j] = Y[j]-1
        X[j] = X[j] + V_X[j]*t
        Y[j] = Y[j] + V_Y[j]*t
        circle(screen, COLOR[j], (X[j], Y[j]), R[j])
    pygame.display.update()
    

def check_click():
    global score
    for j in range (k):
        if R[j] - ((event.pos[0]-X[j])**2+(event.pos[1]-Y[j])**2)**0.5 > 0:
         score += 1
         print(score)
         circle(screen, BLACK, (X[j], Y[j]), R[j])
         X.pop(j)
         Y.pop(j)
         R.pop(j)
         V_Y.pop(j)
         V_X.pop(j)
         COLOR.pop(j)
         new_ball()
                    
def create_k_balls():
    global u
    while u<k:
        new_ball()
        u += 1

def write_score():
    ''' '''
    file.write(name)
    file.write(' - ')
    file.write(time.ctime())
    file.write(' - Счет: ')
    file.write(str(score))
    file.write('\n')
    file.close()


pygame.display.update()
clock = pygame.time.Clock()
procces = True

print('Ваше имя, и любимое блюдо?')
name = input()
print('Сколько шариков будет в игре? (введите число)')
k = int(input())

create_k_balls()

while procces:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            procces = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
           check_click()              
    move_balls()
            
    
write_score()
pygame.quit()

##### сделать вывод таблицы лучших игроков, ***сделать счет прямо в игре***, добавить другие мишени, задокументировать
