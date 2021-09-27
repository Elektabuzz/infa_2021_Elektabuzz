import turtle as t
import numpy as np

t.shape('turtle')
t.speed(0)

def cleft(r):
    for i in  range(180):
        t.forward(r * np.sin(np.pi/90))
        t.left(2)
        
def cright(r):
    for i in  range(180):
        t.forward(r * np.sin(np.pi/90))
        t.right(2)

t.left(90)
for x in range (50, 200, 20):
    cleft(x)
    cright(x)
    
