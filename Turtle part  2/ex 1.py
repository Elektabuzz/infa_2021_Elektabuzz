import random as r
import  turtle as t

t.speed(0)
t.shape('turtle')
t.color('red')

x=1
while x < 200:
    t.right(r.randint(-180,180))
    t.forward(r.randint(4,40))
    x+=1


