import turtle
"""
while(True): #КВАДРАТ
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)

while(True): #S
    turtle.shape('turtle')
    turtle.speed(2)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(150)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.pendown()


while(True): #КРУГ
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.circle(150)

while(True): #КРУГ2
turtle.shape('turtle')
turtle.speed(10)
for i in range(361):
    turtle.forward(1)
    turtle.right(1)


import turtle #10 КВАДРАТОВ В КВАДРАТЕ

frw = 20
x = 0
y = 0
for i in range(10):
    turtle.shape('turtle')
    turtle.speed(10)
    for i in range(4):
        turtle.forward(frw)
        turtle.left(90)
    frw += 20
    x -= 10
    y -= 10
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
turtle.mainloop()
"""

import turtle # Паук с 12 лапами

turtle.shape("turtle")
turtle.speed(2)
for i in range(12):
    for j in range(1):
        turtle.right(360/12)
        turtle.forward(80)
        turtle.stamp()
        turtle.goto(0, 0) # черепашка запоминает позицию в градусах

turtle.mainloop()
