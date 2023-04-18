# Prisha Patel
# Loops (For & While)
# COP 2500 0001
# September 7, 2022

import random

num = int(input("Guess a number\n"))
goal = random.randint(1,100)

while (num != 10):
    print("Wrong number")
    if (num < goal):
        print("You guessed to low")
    elif (num > goal):
        print("You guessed to high")
        
    num = int(input("Guess another number\n"))
    
print("You got it right")
