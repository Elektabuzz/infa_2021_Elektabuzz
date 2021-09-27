import turtle
from random import randint


number_of_turtles = 10
steps_of_time_number = 200

I=[turtle.Turtle(shape='turtle') for i in range(1)]
for turtl in I:
    turtl.width(5)
    turtl.speed(0)
    turtl.penup()
    turtl.goto(-204,-204)
    turtl.pendown()
    for a in range(4):
        turtl.forward(408)
        turtl.left(90)
    turtl.penup()
    turtl.goto(10000,10000)

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

Vx=[0]*len(pool)
Vy=[0]*len(pool)
n=0

for unit in pool:
    unit.color('blue')
    unit.shapesize(0.5)
    Vx[n]=randint(-50,50)
    Vy[n]=randint(-50,50)
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))
    n+=1


for i in range(steps_of_time_number):

    t=0.15
    k=0
    
    for unit in pool:
        
        x,y = unit.pos()
        x=x+t*Vx[k]
        y=y+t*Vy[k]
        unit.goto(x,y)
        if abs(y)>200:
            Vy[k]=-1*Vy[k]
        if abs(x)>200:
            Vx[k]=-1*Vx[k]
        k+=1
