# Prisha Patel
# Vehicle
# COP 2500 0001
# September 9, 2022

# make whatever vehicle you want, do not need color
# outline of any vehicle, close enough = good to go
# put some comments on the code like this to explain what part of the car draws what
# use 20 commands
# forward, left, forward is three commands, but it can be forward then forward

import turtle

turtle.speed(6)

# Left Wheel
turtle.penup()
turtle.goto(-150,-100)
turtle.pendown()

turtle.circle(-50,360)

turtle.penup()
turtle.goto(-150,-125)
turtle.pendown()

turtle.circle(-25,360)


# Right Wheel
turtle.penup()
turtle.goto(150,-100)
turtle.pendown()

turtle.circle(-50,360)

turtle.penup()
turtle.goto(150,-125)
turtle.pendown()

turtle.circle(-25,360)

# Giant bus body outline
turtle.penup()
turtle.goto(-100,-165)
turtle.pendown()

turtle.forward(205)

turtle.penup()
turtle.goto(200,-165)
turtle.pendown()

turtle.forward(50)
turtle.left(90)
turtle.forward(270)
turtle.left(90)
turtle.forward(520)
turtle.left(90)
turtle.forward(145)
turtle.right(60)
turtle.forward(80)
turtle.left(60)
turtle.forward(85)
turtle.left(90)
turtle.forward(150)


# Windows on the bus
turtle.penup()
turtle.goto(-250,-10)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)

turtle.penup()
turtle.goto(-150,-10)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)

turtle.penup()
turtle.goto(-50,-10)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)

turtle.penup()
turtle.goto(50,-10)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)

turtle.penup()
turtle.goto(150,-10)
turtle.pendown()

turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(75)
turtle.left(90)







