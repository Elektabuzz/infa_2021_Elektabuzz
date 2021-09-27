file = open('ex3.txt','w')

s='''import turtle as t
import numpy as np
t.shape('turtle')

a=40 #длина ребра
b=a/8*5 # интервал между цифрами
s=np.sqrt(2)# корень из двух

def zero(x):
    for i in 0,0:
        t.forward(a)
        t.right(90)
        t.forward(2*a)
        t.right(90)
    t.penup()
    t.forward(a+b)
    t.pendown()
    

def one(x):
    t.penup()
    t.right(90)
    t.forward(a)
    t.pendown()
    t.left(135)
    t.forward(s*a)
    t.right(135)
    t.forward(2*a)
    t.penup()
    t.backward(2*a)
    t.left(90)
    t.forward(b)
    t.pendown()
    
def two(x):
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(45)
    t.forward(s*a)
    t.left(135)
    t.forward(a)
    t.penup()
    t.left(90)
    t.forward(2*a)
    t.right(90)
    t.forward(b)
    t.pendown()

def three(x):
    for i in 0,0:
        t.forward(a)
        t.right(135)
        t.forward(s*a)
        t.left(135)
    t.penup()
    t.forward(a)
    t.left(90)
    t.forward(2*a)
    t.right(90)
    t.forward(b)
    t.pendown()

def four(x):
    t.right(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.backward(a)
    t.forward(2*a)
    t.right(90)
    t.penup()
    t.forward(b)
    t.pendown()

def five(x):
    t.penup()
    t.right(90)
    t.forward(2*a)
    t.pendown()
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(a)
    t.penup()
    t.forward(b)
    t.pendown()

def six(x):
    t.penup()
    t.right(90)
    t.forward(a)
    t.pendown()
    for i in range(4):
        t.forward(a)
        t.left(90)
    t.left(135)
    t.forward(s*a)
    t.right(45)
    t.penup()
    t.forward(b)
    t.pendown()

def seven(x):
    t.forward(a)
    t.right(135)
    t.forward(s*a)
    t.left(45)
    t.forward(a)
    t.penup()
    t.left(90)
    t.forward(a)
    t.left(90)
    t.forward(2*a)
    t.right(90)
    t.forward(b)
    t.pendown()

def eight(x):
    zero()
    t.penup()
    t.backward(a+b)
    t.pendown()
    four()

def nine(x):
    t.right(90)
    t.penup()
    t.forward(2*a)
    t.pendown()
    t.left(135)
    t.forward(s*a)
    t.left(45)
    for  i in range(5):
        t.forward(a)
        t.left(90)
    t.right(180)
    t.penup()
    t.forward(b)
    t.pendown() '''

file.write(s)
file.close()
