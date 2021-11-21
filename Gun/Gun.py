import math
from random import choice
from random import randint
import pygame

FPS = 30
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

width_of_window = 800
height_of_window = 600
v_max: int = 35


class Ball:
    def __init__(self, gun, live=3, k=0.9):

        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        live - количество ударов мяча до его исчезновения
        k - отношение модуля скорости мяча после удара и до
        """
        self.k = k
        self.ball_screen = screen
        self.x = gun.x1
        self.y = gun.y1
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = live

    def draw(self):
        """Функция рисует мяч"""
        pygame.draw.circle(self.ball_screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли мяч с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if math.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= (self.r + obj.r):
            return True
        else:
            return False


class FirstTypeBullet(Ball):
    def move(self):
        """Перемещение мяча по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """

        self.x += self.vx
        self.y -= self.vy
        self.vy -= 1
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.k * self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.k * self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.k * self.vy
        elif (self.y + self.r) > height_of_window:
            self.live -= 1
            self.vy = -self.k * self.vy
            self.y = height_of_window - self.r


class SecondTypeBullet(Ball):
    def move(self):
        """Перемещение мяча по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна.
        """

        self.x += self.vx
        self.y -= self.vy
        self.vy -= 5
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.k * self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.k * self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.k * self.vy
        elif (self.y + self.r) > height_of_window:
            self.live -= 3
            self.vy = -self.k * self.vy
            self.y = height_of_window - self.r


class Gun:
    def __init__(self, scores=0, x1=40, y1=450, x2=50, y2=450, width=10):
        """ Конструктор класса Gun
        Args:
        x1 - положение одного конца по горизонтали
        y1 - положение одного конца по вертикали
        x2 - положение другого конца горизонтали
        y2 - положение другого конца по вертикали
        width - ширина пушки
        """
        self.scores = scores
        self.gun_screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.color2 = GREEN
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.width = width
        self.d = 80
        self.h = 80
        self.vx = 5
        self.vy = 5

    def fire2_start(self):
        """Запускание подготовки к выстрелу"""
        self.f2_on = 1

    def fire2_left_end(self, end_event, array_balls):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        Args:
            end_event - событие отпускания мыши
            *array_balls - массив мячей
        """
        new_ball = FirstTypeBullet(gun)
        self.an = math.atan2((end_event.pos[1] - new_ball.y), (end_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        array_balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def fire2_right_end(self, end_event, array_balls):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        Args:
            end_event - событие отпускания мыши
            *array_balls - массив мячей
        """
        new_ball = SecondTypeBullet(gun)
        self.an = math.atan2((end_event.pos[1] - new_ball.y), (end_event.pos[0] - new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        array_balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, targetting_event):
        """Прицеливание. Зависит от положения мыши.
        Args:
            targetting_event - событие изменение позиции мыши
        """
        if targetting_event:
            self.an = math.atan((targetting_event.pos[1] - self.y1) / (targetting_event.pos[0] - (self.x1 - 20)))
            self.x2 = self.x1 + self.f2_power * math.cos(self.an)
            self.y2 = self.y1 + self.f2_power * math.sin(self.an)
            if targetting_event.pos[0] - (self.x1 - 20) > 0:
                self.x2 = self.x2
                self.y2 = self.y2
            else:
                self.x2 = 2*self.x1 - self.x2
                self.y2 = 2*self.y1 - self.y2

        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        """Функция рисует пушку"""
        pygame.draw.rect(self.gun_screen, self.color2, (self.x1 - 40, self.y1 - 40, self.d, self.h))
        pygame.draw.line(self.gun_screen, self.color, (self.x1, self.y1), (self.x2, self.y2), self.width)

    def power_up(self):
        """увеличивает начальную скорость мяча и длину пушки, меняет цвет пушки в зависимости от длительности нажатия"""
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY

    def hit_first_type_bullet(self, obj, points=1):
        """Попадание шарика в цель.
        Args:
            points - шаг изменения количества очков при попадании в цель
            obj - объект
        """
        if type(obj) == FirstTypeTarget:
            self.scores += points
        elif type(obj) == SecondTypeTarget:
            self.scores += 2 * points
        else:
            print('Вы попали не в мишень')
        print('scores:', self.scores)
        return self.scores

    def hit_second_type_bullet(self, obj, points=3):
        """Попадание шарика в цель.
        Args:
            points - шаг изменения количества очков при попадании в цель
        """
        if type(obj) == FirstTypeTarget:
            self.scores += points
        elif type(obj) == SecondTypeTarget:
            self.scores += 2 * points
        else:
            print('Вы попали не в мишень')
        print('scores:', self.scores)
        return self.scores

    def move_d(self):
        """
        Двигает танк вправо
        """
        self.x1 += self.vx

    def move_a(self):
        """
        Двигает танк влево
        """
        self.x1 -= self.vx

    def move_w(self):
        """
        Двигает танк вверх
        """
        self.y1 -= self.vy

    def move_s(self):
        """
        Двигает танк вниз
        """
        self.y1 += self.vy


class Target:
    def __init__(self, live=1):
        """ Конструктор класса ball
        Args:
            scores - количество заработанных очков
            live - приобретает значение 0 при попадании в цель, 1 - когда цель существует
        """

        self.target_screen = screen
        self.live = live
        self.x = randint(600, 780)
        self.y = randint(300, 550)
        self.r = randint(2, 50)
        self.vx = randint(-10, 10)
        self.vy = randint(-10, 10)
        self.color = RED

    def draw(self):
        """Функция рисует объект"""
        pygame.draw.circle(self.target_screen, self.color, (self.x, self.y), self.r)


class FirstTypeTarget(Target):
    def move(self):
        """Перемещение цели по прошествии единицы времени"""
        self.x += self.vx
        self.y -= self.vy
        if (self.x - self.r) < 0:
            self.x = self.r
            self.vx = -self.vx
        elif (self.x + self.r) > width_of_window:
            self.vx = -self.vx
            self.x = width_of_window - self.r
        if (self.y - self.r) < 0:
            self.y = self.r
            self.vy = -self.vy
        elif (self.y + self.r) > height_of_window:
            self.vy = -self.vy
            self.y = height_of_window - self.r


class SecondTypeTarget(Target):
    def move(self):
        """Перемещение цели по прошествии единицы времени"""

        self.x += self.vx
        self.y -= self.vy
        if (self.x - self.r) < 0:
            self.x = self.r
            if abs(self.vx) <= v_max:
                self.vx = -2 * self.vx
            else:
                self.vx = -self.vx
        elif (self.x + self.r) > width_of_window:
            self.x = width_of_window - self.r
            if abs(self.vx) <= v_max:
                self.vx = -2 * self.vx
            else:
                self.vx = -self.vx
        if (self.y - self.r) < 0:
            self.y = self.r
            if abs(self.vy) <= v_max:
                self.vy = -2 * self.vy
            else:
                self.vy = -self.vy
        elif (self.y + self.r) > height_of_window:
            if abs(self.vy) <= v_max:
                self.vy = -2 * self.vy
            else:
                self.vy = -self.vy
            self.y = height_of_window - self.r


pygame.init()
screen = pygame.display.set_mode((width_of_window, height_of_window))

first_type_bullets = []
second_type_bullets = []

clock = pygame.time.Clock()
gun = Gun()
target1 = FirstTypeTarget()
target2 = SecondTypeTarget()
finished = False
flD = flA = flW = flS = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target1.draw()
    target2.draw()
    for i in first_type_bullets:
        i.draw()
    for i in second_type_bullets:
        i.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                gun.fire2_left_end(event, first_type_bullets)
            elif event.button == 3:
                gun.fire2_right_end(event, second_type_bullets)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                flD = True
            elif event.key == pygame.K_a:
                flA = True
            elif event.key == pygame.K_w:
                flW = True
            elif event.key == pygame.K_s:
                flS = True
        elif event.type == pygame.KEYUP:
            flD = flA = flW = flS = False
        elif flD:
            gun.move_d()
        elif flA:
            gun.move_a()
        elif flW:
            gun.move_w()
        elif flS:
            gun.move_s()

    target1.move()
    target2.move()

    for i in first_type_bullets:
        i.move()
        if i.hittest(target1):
            target1.live = 0
            gun.hit_first_type_bullet(target1)
            target1 = FirstTypeTarget()
        else:
            if i.hittest(target2):
                target2.live = 0
                gun.hit_first_type_bullet(target2)
                target2 = SecondTypeTarget()
        if i.live <= 0:
            first_type_bullets.pop(first_type_bullets.index(i))

    for i in second_type_bullets:
        i.move()
        if i.hittest(target1):
            target1.live = 0
            gun.hit_second_type_bullet(target1)
            target1 = FirstTypeTarget()
            second_type_bullets.pop(second_type_bullets.index(i))
        else:
            if i.hittest(target2):
                target2.live = 0
                gun.hit_second_type_bullet(target2)
                target2 = SecondTypeTarget()
                second_type_bullets.pop(second_type_bullets.index(i))
        if i.live <= 0:
            second_type_bullets.pop(second_type_bullets.index(i))

    gun.power_up()

pygame.quit()
