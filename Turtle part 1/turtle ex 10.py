import turtle as t
import numpy as np

t.shape('turtle')
t.speed(0)

def circle(r):
    for i in  range(360):
        t.forward(r * np.sin(np.pi/180))
        t.left(1)

for i in range (6):
    circle(70) #Лепестки будут иметь радиус 70
    t.left(360 / 6)
