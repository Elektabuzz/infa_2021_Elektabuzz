import turtle as t
import numpy as np

t.shape('turtle')
t.speed(0)

def cl(r): #cl=cirle left
    for i in  range(180):
        t.forward(r * np.sin(np.pi/90))
        t.left(2)
        
def cr(r): #cr=cirle right
    for i in  range(180):
        t.forward(r * np.sin(np.pi/90))
        t.right(2)

def hc(r): #hc=half circle
    for i in range(90):
        t.forward(r * np.sin(np.pi/90))
        t.right(2)

t.penup()
t.goto(120,0)
t.pendown()

#Фон
t.left(90)
t.color('black','yellow')
t.begin_fill()
cl(120)
t.end_fill()
t.right(90)

#Глаза
for i in [-1,1]:
    t.penup()
    t.goto(i*40,50)
    t.pendown()
    t.color('black','blue')
    t.begin_fill()
    cl(20)
    t.end_fill()

#Нос
t.right(90)
t.penup()
t.goto(0,35)
t.pendown()
t.width(12)
t.forward(35)

#Рот
t.penup()
t.goto(70,0)
t.pendown()
t.width(15)
t.color('red')
hc(70)
