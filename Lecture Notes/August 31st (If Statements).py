# Prisha Patel
# If statements
# COP 2500 0001
# August 31, 2022

# if statements are taking the program from being a calcultor to able to make decisions

temp = int(input("What is the temperature outside?\n"))

# < - less than
# > - greater than
# <= - less than or equal to
# >= - greater than or equal to
# == - equal to
# != - not equal to

# () in the if statements above is not required but better to get accustomed to it due to other programming languages
if (temp < 70):
    print("Its pretty cold but I can handle only so much.\n")

if (temp < 40):
    print("It's way to freaking cold.\n")

# if there is an extra space in the beginning line, the code is broken, make sure everything is perfectly aligned to make sure your code works
print("ELSE IF STATEMENT\n")


if (40 <= temp <70):
    print("Its pretty cold but I can handle only so much.\n")
elif (temp < 40):
    print("It's way to freaking cold.\n")

if (temp < 40):
    print("It's way to freaking cold.\n")
elif (temp < 70):
    print("It's pretty cold but I can only handle so much.\n")

# AND OR STATEMENTS
if (40 <= temp and temp < 70):
    print("It's pretty cold but I can only handle so much.\n")
elif (temp < 40):
    print("It's way to freaking cold.\n")
# this code below is broken
if (40 <= temp or temp < 70):
    print("It's pretty cold but I can only handle so much.\n")
elif(temp < 40):
    print("It's way to freaking cold.\n")

# you need to have an equal sign for this statementto work
if not (temp < 70):
    print()
if (temp >= 70):
    


#

grade = float(input("What is your grade?\n"))

if (grade >= 90):
    print("A")
elif (grade >= 80):
    print("B")
elif (grade >= 70):
    print("C")
else:
    print("F")

# all the "else" you read it as otherwise

if (grade >= 90):
    print("A")
if (80 <= grade < 90):
    print("B")
if (70 <= grade < 80):
    print("C")
if (grade < 70):
    print ("F")


if (grade >= 90):
    print("A")
elif (80 <= grade < 90):
    print("B")
elif (70 <= grade < 80):
    print("C")
elif (grade < 70):
    print ("F")



















    
                    
