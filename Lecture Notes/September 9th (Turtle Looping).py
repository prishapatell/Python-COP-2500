# Prisha Patel
# Turtle Looping
# COP 2500 0001
# September 9, 2022

import turtle

turtle.speed(9)

number = 10

while (number > 0):
    turtle.forward(50)
    turtle.left(36)
    print(number)
    number = number - 1
# Without the = sign the number is not being set
    
side = 6
number = side

while (number > 0):
    turtle.forward(50)
    turtle.left(360/side)
    print(number)
    number = number - 1

side = 12
number = 0

while (number < side):
    turtle.forward(50)
    turtle.left(360/side)
    print(number)
    number = number + 1

turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
print("For Loops")
for count in range(5):
    print(count)
    turtle.forward(50)
    turtle.left(72)
# we do 360/ number to get how many side needed for a shape

# turtle.speed(1-10)
# speed fastest is not 10 but 0 and normal is 6

turtle.penup()
turtle.goto(-200,-100)
turtle.pendown()

for count in range(20):
    turtle.forward(50)
    turtle.left(100)

# Midterm First Week of October
