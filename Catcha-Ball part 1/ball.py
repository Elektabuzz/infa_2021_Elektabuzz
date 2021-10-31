import pygame
from pygame.draw import *
from random import randint
import time
pygame.init()

#a,b, FPS - ширина и высота экрана в пикселях, а также кол-во кадров в секунду
FPS = 30
a = 1000
b = 700
screen = pygame.display.set_mode((a,b))

#Создает необходимые переменные и массивы, для дальнейшего использования
X = []
V_X = []
Y = []
V_Y = []
R = []
COLOR = []
t = 1
score = 0
u=0

#Цвета для игры
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]




def new_ball():
    '''Создает новый шар, и записывает его характеристики в соответствующие массивы'''
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

    
    
def move_items():
    '''Передвигает все созданные объекты. при необходимости обеспечивает случайное отражение от
       стен.в этой функции используется t, от которой зависит величина перемещения между кадрами
       a,b - ширина и высота рабочей области приложения.'''
    for j in range (k):
        circle(screen, BLACK, (X[j], Y[j]), R[j])
        if X[j]-R[j] <= 0:
            V_X[j] = randint(1, 7)
            V_Y[j] = randint(-7, 7)
            X[j] = 0 + R[j]
        elif X[j] + R[j] >= a:
            V_X[j] = randint(-7, -1)
            V_Y[j] = randint(-7, 7)
            X[j] = a - R[j]
        elif Y[j]- R[j] <= 0:
            V_Y[j] = randint(1, 7)
            V_X[j] = randint(-7, 7)
            Y[j] = 0 + R[j]
        elif Y[j]+R[j] >= b:
            V_Y[j] = randint(-7, -1)
            V_X[j] = randint(-7, 7)
            Y[j] = b - R[j]
        X[j] = X[j] + V_X[j]*t
        Y[j] = Y[j] + V_Y[j]*t
        circle(screen, COLOR[j], (X[j], Y[j]), R[j])
    pygame.display.update()
    

def check_click():
    '''Проверяет, попал ли игрок по мишеням. При попадании создает новую мишень'''
    global score
    for j in range (k):
        if R[j] - ((event.pos[0]-X[j])**2+(event.pos[1]-Y[j])**2)**0.5 > 0:
            score += 1
            print("Вы попали!!! Теперь ваш счёт: ", score)
            circle(screen, BLACK, (X[j], Y[j]), R[j])
            X.pop(j)
            Y.pop(j)
            R.pop(j)
            V_Y.pop(j)
            V_X.pop(j)
            COLOR.pop(j)
            new_ball()
            
                    
def create_k_balls():
    '''создает k шаров'''
    global u
    while u<k:
        new_ball()
        u += 1


pygame.display.update()
clock = pygame.time.Clock()
procces = True


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
    move_items()

            
pygame.quit()

