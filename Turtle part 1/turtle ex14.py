import turtle as t
import numpy as np

t.shape('turtle')

def star(n): 
        a=(180/n)
        l=140
        t.left(90 + a/2)
        for i in range (n):
            t.forward(l)
            t.left(180-a)
        t.right(90 + a/2)
        

star(5)
t.penup()
t.goto(150,0)
t.pendown()
star(11)
