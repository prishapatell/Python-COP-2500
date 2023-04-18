# Prisha Patel
# COP 2500
# Assignment 5.1 
# November 11, 2022

import math
import turtle
import random

def distance(x, y):
  dis_for = math.sqrt((x-0)**2+(y-0)**2)
  return dis_for

# Starter Code
def randomTurtle():
 for count in range(10):
   choice = random.randint(1,2)
   if (choice==1):
     turtle.forward(random.randint(5, 50))
   elif(choice==2):
     turtle.right(random.randint(1,359))

def testTurtle():
 turtle.forward(100)
 turtle.left(90)
 turtle.forward(100)
# Call this when turning it in
randomTurtle()
# Call this when testing to make sure you have the correct answer
# testTurtle()

print(distance(turtle.xcor(),turtle.ycor()))