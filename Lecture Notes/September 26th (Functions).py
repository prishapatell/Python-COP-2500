# Prisha Patel
# Functions
# COP 2500 0001
# September 26, 2022

# FROM HERE TO END OF SEMESTER WILL BE ON FINAL
# BUT IT BUILDS OFF OF THE FIRST 5 WEEKS

import turtle
import random


def draw_box(x,y, size):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    
    for num in range(4):
        turtle.forward(size)
        turtle.left(90)


def draw_star():
# def = define (not calling)
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(100)
        turtle.left(135)
    turtle.end_fill()

def draw_star():
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(size)
        turtle.left(135)
    turtle.end_fill()

def draw_star(size,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

    low = y
    
    turtle.begin_fill()
    for x in range(8):
        turtle.forward(size)
        turtle.left(135)
        # check to see if it is lower than low
        pos = turtle.pos()
        y = pos[1]
        low = min(low,y)
        print(low)
    turtle.end_fill()
    return low


turtle.speed(0)

for num in range(10):
    size = random.randint(50,200)
    x = random.randint(-300,300)
    y = random.randint(-300,300)


    new_y = draw_star(size, x, y)
    draw_box(x,new_y,size)
