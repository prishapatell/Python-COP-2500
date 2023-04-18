# Prisha Patel
# Lab 2 Challenge 3
# COP 2500 0001
# September 6, 2022

# Input

print("Where would you like to go?")
print("1. Beach")
print("2. Theme Park")

choice = int(input("Where are you going: "))
if (choice == 1): # Beach
    print("How many beach balls do you have?")
    choice = int(input("How many: "))

    if (choice >= 5):
        print("You are well prepared.")
    elif (choice < 5):
        print("Are you sure you have enough?")
else: # Theme Park
    print("How many people are there?")
    choice = int(input("How many: "))

    if (choice >= 1000):
        print("This is to crowded.")
    elif (500 <= choice < 999):
        print("It's going to be busy.")
    elif (100 <= choice < 499):
        print("Its a light day.")
    else:
        print("Nobody is here.")
        
