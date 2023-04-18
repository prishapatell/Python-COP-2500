# Prisha Patel
# Math, Rounding, 
# COP 2500 0001
# September 12, 2022


#   Check out python math module
#   Anything we import, we cannot put that name as the file name

import math

# This fucntion will be mostly used during situations regarding money.
gpa = 3.91276
# print out gpa with one decimal digit
print("Your gpa is","%.1f"%gpa, "trailing message")
# print out gpa with two decimal digits
print("Your gpa is","%.2f"%gpa, "trailing message")

# Exponenets
value = 8**2
print(value)
# pow = exponent
value = math.pow(8,2)
print(value)

# Absoulte Value
# sqrt = square root
value = math.sqrt(64)
print(value)

# Absolute Value
# fabs = float absolute value
value = math.fabs(-5)
print(value)
value = math.fabs(-25)
print(value)
value = math.fabs(25)
print(value)

# Rounding
value = round(3.923456789)
print(value)
value = round(3.923456789,2)
print(value)
value = round(3.900000002,2)
print(value,"%.2f"%value)

# Rounding Up
value = math.ceil(2.8)
print(value)

# Rounding Down
value = math.floor(36.75)
print(value)

# pi
print(math.pi)

# Golf Example
import random

distance = random.randint(15,25)
print("You are", distance, "feet away")
score = 0

while(distance > 0):
    print("How hard would you like to hit it")
    print("1. Lightly")
    print("2. Kinda light")
    print("3. Kinda Hard")
    print("4. Hard")
    hit = int(input("What do you choose"))
    score += 1

    if(hit==1):
        distance = distance - random.randint(1,2)
    if(hit==2):
        distance = distance - random.randint(3,8)
    if(hit==3):
        distance = distance - random.randint(5,15)
    if(hit==4):
        distance = distance - random.randint(10,30)

    distance = int(math.fabs(distance))

    print("You are", distance, "feet away")
    print("You scored at", score)











































