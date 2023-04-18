# Friday - Review Days

# Question 1
# I don't
# need "help"
print("I don\'t \nneed \"help\"")
print("I don't \nneed \"help\"")
print('I don\'t \nneed help')

# Question 2
# The name of the car you drive
car = str(input("The name of your car:\n"))
car = input("The name of your car:\n")
print(car)
# The number of passengers your car can hold
passengers = int(input("Number of passenegers:\n"))
print(passengers)
# Your average miles per gallon your car gets
mpg = float(input("Average miles per gallon:\n"))
print(mpg)

# Question 3
value = 4
if(value <= 3):
    value += 5
    if(value > 5):
        value += 5
    else:
        value = value - 1
else:
    value -= 5
    if(value >= 3):
        value = 5

# Question 4
# Part 1
x = 7
for num in range(11,15,2):
    x += 1
print(x)
# Part 2
x = 0
for num in range(2,5):
    x = x + num + 1
print(x)
# Part 3
x = 0
num = 6
while (num != 10):
    if (num < 10):
        num += 5
    elif (num > 10):
        num -= 2
    x += 1
print(x)

# Question 5
# Kyle likes season 1-4
# Juila likes season 13 and 26+
season = int(input("Which season do you like"))
if (season <= 4):
    print("Kyle")
elif(season == 13 or season >= 26):
    print("Julia")
else:
    print("Neither")
# OR
if (season <= 4):
    print("Kyle")
elif(season == 13):
    print("Julia")
elif(season >= 26):
    print("Julia")
else:
    print("Neither")

# Question 6
quote = []
for index in range(len(quote)):
    if index % 2 == 0:
        quote[index] = quote[index].lower()
    else:
        quote[index] = quote[index].upper()

# Question 7
import turtle
turtle.forward(100)
turtle.right(45)
turtle.penup()
turtle.forward(100)
turtle.pendown()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
