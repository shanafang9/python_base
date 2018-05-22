# coding:utf-8

import turtle


turtle.showturtle()

# turtle.goto(50,40)

# turtle.color('red','yellow') # 等价 turtle.color('turtle.pencolor()','turtle.fillcolor')

turtle.pencolor('red')
turtle.fillcolor('yellow')

turtle.begin_fill()

# turtle.pensize(5)
# turtle.circle(30)
turtle.goto(80,0)
turtle.penup()
turtle.goto(40,40)
turtle.pendown()
turtle.goto(80,0)
turtle.penup()
turtle.goto(40,40)
turtle.pendown()
turtle.goto(0,0)

turtle.end_fill()

turtle.done()