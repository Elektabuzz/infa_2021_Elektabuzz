import turtle as t

t.shape('circle')
t.speed(0)

x=0
y=0.1
Vx=5
Vy=20
ay=-1

dt=0.1
for i in range(4000):
    if y>=0:
        x+= Vx*dt
        y+= Vy*dt + ay*dt**2/2
        Vy+= ay*dt
        t.goto(x,y)
    else:
        Vy=-0.8*Vy
        y=0.1
        x+= Vx*dt
        y+= Vy*dt + ay*dt**2/2
        Vy+= ay*dt
        t.goto(x,y)
