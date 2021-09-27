import turtle as t
import numpy as np

t.shape('turtle')
t.speed(0)

def hc(r): #hc=half circle
    for i in range(90):
        t.forward(r * np.sin(np.pi/90))
        t.right(2)


t.left(90)
for x in range(7):
    hc(40)
    hc(10)


        

    
