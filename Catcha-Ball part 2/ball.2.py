import pygame
from pygame.draw import *
from random import randint
import time

pygame.init()

# a,b, FPS - ширина и высота экрана в пикселях, а также кол-во кадров в секунду
FPS = 30
a = 1000
b = 700
screen = pygame.display.set_mode((a, b))

# Создает необходимые переменные и массивы, для дальнейшего использования
X = []
V_X = []
Y = []
V_Y = []
R = []
COLOR = []
Xc = []
V_Xc = []
Yc = []
V_Yc = []
Rc = []
COLORc = []
Dc = []
t = 1
score = 0
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
NAME = []
SCORE = []


def new_ball():
    """Создает новый шар, и записывает его характеристики в соответствующие массивы
    """
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


def new_circle():
    """Создает новую окружность, и записывает её характеристики в соответствующие массивы
    """
    global x, y, r, v_x, v_y, color, i, d
    x = randint(100, 900)
    v_x = randint(-7, 7)
    v_y = randint(-7, 7)
    y = randint(100, 600)
    r = randint(30, 100)
    d = randint(14, 24)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r, d)
    pygame.display.update()
    Xc.append(x)
    V_Xc.append(v_x)
    Yc.append(y)
    V_Yc.append(v_y)
    Rc.append(r)
    Dc.append(d)
    COLORc.append(color)


def move_items():
    """Передвигает все созданные объекты. при необходимости обеспечивает отражение от стен.
       в этой функции используется t, от которой зависит величина перемещения между кадрами
       a,b - ширина и высота рабочей области приложения. Для окружностей меняются скорости
       с каждым применением функции.
       """
    screen.fill(BLACK)
    for j in range(k):
        if X[j] - R[j] <= 0:
            V_X[j] = randint(1, 7)
            V_Y[j] = randint(-7, 7)
            X[j] = 0 + R[j]
        elif X[j] + R[j] >= a:
            V_X[j] = randint(-7, -1)
            V_Y[j] = randint(-7, 7)
            X[j] = a - R[j]
        elif Y[j] - R[j] <= 0:
            V_Y[j] = randint(1, 7)
            V_X[j] = randint(-7, 7)
            Y[j] = 0 + R[j]
        elif Y[j] + R[j] >= b:
            V_Y[j] = randint(-7, -1)
            V_X[j] = randint(-7, 7)
            Y[j] = b - R[j]
        X[j] = X[j] + V_X[j] * t
        Y[j] = Y[j] + V_Y[j] * t
        circle(screen, COLOR[j], (X[j], Y[j]), R[j])
    for j in range(m):
        if Xc[j] - Rc[j] <= 0:
            V_Xc[j] = -V_Xc[j]
            Xc[j] = 0 + Rc[j]
        elif Xc[j] + Rc[j] >= a:
            V_Xc[j] = -V_Xc[j]
            Xc[j] = a - Rc[j]
        elif Yc[j] - Rc[j] <= 0:
            V_Yc[j] = -V_Yc[j]
            Yc[j] = 0 + Rc[j]
        elif Yc[j] + Rc[j] >= b:
            V_Yc[j] = -V_Yc[j]
            Yc[j] = b - Rc[j]
        Xc[j] = Xc[j] + V_Xc[j] * t
        Yc[j] = Yc[j] + V_Yc[j] * t
        V_Xc[j] = randint(-20, 20)
        V_Yc[j] = randint(-20, 20)
        circle(screen, COLORc[j], (Xc[j], Yc[j]), Rc[j], Dc[j])
    pygame.display.update()


def check_click():
    """Проверяет, попал ли игрок по мишеням. При попадании создает новую мишень
    """
    global score
    for j in range(k):
        if R[j] - ((event.pos[0] - X[j]) ** 2 + (event.pos[1] - Y[j]) ** 2) ** 0.5 > 0:
            score += 1
            print('Вы попали!!! Теперь ваш счёт: ', score)
            circle(screen, BLACK, (X[j], Y[j]), R[j])
            X.pop(j)
            Y.pop(j)
            R.pop(j)
            V_Y.pop(j)
            V_X.pop(j)
            COLOR.pop(j)
            new_ball()
    for j in range(m):
        if Rc[j] - ((event.pos[0] - Xc[j]) ** 2 + (event.pos[1] - Yc[j]) ** 2) ** 0.5 > 0:
            if Rc[j] - ((event.pos[0] - Xc[j]) ** 2 + (event.pos[1] - Yc[j]) ** 2) ** 0.5 <= Dc[j]:
                score += 3
                print('Вы попали!!! Теперь ваш счёт: ', score)
                circle(screen, BLACK, (Xc[j], Yc[j]), Rc[j], Dc[j])
                Xc.pop(j)
                Yc.pop(j)
                Rc.pop(j)
                V_Yc.pop(j)
                V_Xc.pop(j)
                COLORc.pop(j)
                Dc.pop(j)
                new_circle()


def create_k_balls():
    """создает k шаров
    """
    k_1 = k
    while k_1 > 0:
        new_ball()
        k_1 -= 1


def create_m_circles():
    """создает m окружностей
    """
    m_1 = m
    while m_1 > 0:
        new_circle()
        m_1 -= 1


def write_score():
    """Записывает результат игрока в файл score.txt"""

    file = open('score.txt', 'a')
    file.write('\n')
    file.write(name)
    file.write(' - ')
    file.write(time.ctime())
    file.write(' - Счет: ')
    file.write(str(score))
    file.write('\n')
    file.close()

    file = open('score.txt', 'r')
    players = 0
    while True:
        stroka = file.readline()
        if not stroka:
            break
        if stroka == '\n':
            pass
        else:
            linec = stroka.split(' - Счет: ')
            NAME.append(linec[0])
            SCORE.append(int(linec[1].replace('\n', '')))
            players += 1

    file = open('score.txt', 'w')
    for j in range(players):
        file.write(NAME[SCORE.index(max(SCORE))])
        file.write(' - Счет: ')
        file.write(str(SCORE[SCORE.index(max(SCORE))]))
        file.write('\n')
        SCORE[SCORE.index(max(SCORE))] = -1
    file.close()


pygame.display.update()
clock = pygame.time.Clock()
procces = True

print('Ваше имя')
name = input()
print('Сколько шариков будет в игре? (введите число)')
k = int(input())
print('Сколько мишеней будет в игре? (введите число)')
m = int(input())

create_k_balls()
create_m_circles()

while procces:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            procces = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_click()
    move_items()

write_score()
pygame.quit()
