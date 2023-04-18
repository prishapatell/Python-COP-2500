# Prisha Patel
# Lab 3 Challenge 3
# COP 2500 0001
# September 13, 2022


print("Where would you like to go?")
print("1. Beach")
print("2. Theme Park")
print("3. Science Center")

choice = int(input("Where are you going: "))
# Beach
if (choice == 1):
    print("How many beach balls do you have?")
    balls = int(input("How many: "))

    if (balls >= 5):
        print("You are well prepared.")
    elif (balls < 5):
        print("Are you sure you have enough?")
# Theme Park
elif (choice == 2):
    days = int(input("How many days are you going for? "))
    for day in range(1, days+1, 1):
        print("Day", day, "Park", day)

# Science Center
else:
    answer = str(input("Are you ready to go?\n"))
    while(answer != "ready"):
        answer = str(input("Are you ready to go?\n"))

