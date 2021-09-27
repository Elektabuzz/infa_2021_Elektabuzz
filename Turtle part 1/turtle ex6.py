import turtle as t

t.shape('turtle')
x=0
print('Введите значение n - количество лап паука')
n=int(input())
while x<n:
    t.forward(100)
    t.stamp()
    t.goto(0,0)
    t.left(360 / n)
    x+=1
