# Prisha Patel
# autopolygonator
# COP 2500 0001
# October 1, 2022
# Part 1

#Your AUTOPOLYGONATOR should accept two inputs:

#The number of sides of the polygon
#The total length of the polygon
#The AUTOPOLYGONATOR will then use turtle graphics to draw a polygon with the given number of sides of equal length, connected with equal angles, at the given total length.

#You may assume that all the inputs will make sense (the number of sides will be a whole number at least three, the length won't be so small that the figure won't be visible, et cetera).

#Part 2

#Once you do this, design your your own unique pattern that uses a for loop.  This could use circles, other lines, but it should be unique to you.

import turtle
# Part 1
sides = int(input("The number of sides of the polygon: "))
length = int(input("The total length of the polygon: "))
theta = 360/sides

turtle.speed(7)

for num in range(sides):
    turtle.forward(length)
    turtle.left(theta)
    
# Part 2
radius = 20
for design in range(radius):
    turtle.penup()
    turtle.goto(300,300)
    turtle.pendown()
    turtle.circle(25)
    turtle.forward(radius)
    turtle.left(radius)

    
