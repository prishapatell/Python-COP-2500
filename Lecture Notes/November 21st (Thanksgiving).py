# Prisha Patel
# COP 2500 0001
# November 21, 2022
# Thanksgiving Program

import random

def food_choices():
    print("1. Turkey")
    print("2. Mashed Potatoes")
    print("3. Green Beans")
    print("4. Casserole")
    print("5 Mix my foods. :(")
    return int(input("Enter the number next to the food"))

def get_points():
    if item == 1:
        return 3
    if item == 2:
        return 1
    if():
        return 5
    if ():
        return 15
    return 30
stress_level = random.randint(25,75)
play = True
while stress_level >= 0 and play == True:
    if (stress_level > 25):
        print("You can do this!")
    elif (stress_level >= 10):
        print("It will be ok, Kyle")
    elif (stress_level > 0):
        print("Why don't you take a break?")
    elif (stress_level == 0):
        print("Its enough")

    choice = input("Would you like to stop playing? (Enter yes to stop)\n")
    if choice.lower.strip() == "yes":
        play = False;
    else:
