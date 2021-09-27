import turtle as t
import numpy as np

t.shape('turtle')
t.speed(5)

def ngon(n):
    x=1
    while x<=n:
        t.forward(10*n)
        t.left(360  / n)
        x+=1

for i in range(3,14,1):
    r =  5*i/np.sin(np.pi / i)
    t.penup()
    t.goto(r,0)
    t.pendown()
    t.left(180 - 90*(i-2)/i)
    ngon(i)
    t.right(180 - 90*(i-2)/i)
