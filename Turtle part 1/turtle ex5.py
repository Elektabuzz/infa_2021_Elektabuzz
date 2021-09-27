import turtle as t

t.shape('turtle')
y=0
while y>-100:
    t.penup()    
    t.goto(y,y)
    t.pendown()
    for x in 1,1,1,1:
        t.forward(50-2*y)
        t.left(90)
    y-=10



