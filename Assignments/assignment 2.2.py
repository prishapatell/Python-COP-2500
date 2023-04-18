# Prisha Patel
# Assignment 2.2
# COP 2500 0001
# September 16, 2022

print("Choose which restuarant to go to for your birthday dinner tonight?")
print("1. Chennai Express")
print("2. Mumbai Madness")
print("3. Dheli Deserts")
print("4. The Cheescake Factory")

choice = int(input("Choose which restuarant to go to for your birthday dinner tonight?"))

# Chennai Express
if(choice == 1):
    print("There is a 20 minute wait. Do you want to wait to be seated inside or take the outside table?")
    print("1. Wait the 20 minutes")
    print("2. Take the table outside")
    choice = int(input("What do you choose?: "))
    if(choice == 1):
        print("Congrats you only had to wait 5 minutes and got a free birthday desert on the house!")
    elif(choice == 2):
        print("Oh No! It's starting to rain heavy")
        print("Looks like the birthday dinner is ruined :(")

# Mumbai Madness
elif(choice == 2):
    print("Mumbai Madness is currently doing specials. Would you like to hear what they are?")
    print("1. Yes")
    print("2. No")
    choice = int(input("What do you choose?: "))
    if(choice == 1):
        print("We have state of the art Fish Filet all the way from France and Fried Chicken all the way from Korea.")
        print("What would you like?: ")
        print("1. Filet 2. Chicken or 3. Neither? ")
        choice = int(input("What do you choose?: "))
        if(choice == 1):
            print("One Fish Fillet from France coming right up!")
        if(choice == 2):
            print("I apologise we just ran out of the Fried Chicken all the way from Korea. :(")
        if(choice == 3):
            print("If neither, then would the Biryani and Chicken Tandori all they way from India be ok? ")
            print("1. Yes")
            print("2. No")
            choice = int(input("What do you choose?: "))
            if(choice == 1):
                print("Here is your Biryani and Chicken Tandori, enjoy!")
            else:
                print("Sorry this restuarant may not be the place for you to have your birthday dinner. :(")
    else:
        print("Sorry this restuarant may not be the place for you to have your birthday dinner. :(")

# Dheli Deserts
elif(choice == 3):
    print("You decided to eat deserts for your sweet birthday? What desert are you craving the most ")
    print("1. Cake")
    print("2. Donut")
    print("3. Macaroon")
    print("4. Eclairs")
    choice = int(input("What do you choose?: "))
    if(choice == 1):
        print("We have three flavors to choose from!")
        print("1. Chocolate")
        print("2. Red Velvet")
        print("3. Funfetti")
        print("Which flavor would you like? ")
        choice = int(input("What do you choose?: "))
        if(choice == 1):
            print("Alrighty here is your chocolate cake enjoy!")
        elif(choice == 2):
            print(" Here you are one red velvet cake!")
        else:
            print("Sorry Funfetti is currently sold out and won't be back until next month. :(")
    elif(choice == 2):
        print("We only give donuts to ages 4-10, sorry no donut for you")
    elif(choice == 3):
        print("We have a wide selection of macaroons which one would you like? ")
        print("1. Strawberry Lemonade")
        print("2. Espresso")
        print("3. Rose")
        print("4. Coconut Pineapple")
        print("5. Chocolate")
        choice = int(input("What do you choose?: "))
        if(choice == 1):
            print("Strawberry lemonade is one of our unique flavors, tell us if you like it.")
        elif(choice == 2):
            print("Espresso is always a clasic, a solid choice indeed.")
        elif(choice == 3):
            print("Rose is our top seller, you indeed made the best choice!")
        elif(choice == 4):
            print("Coconut Pineapple is a flavor that only some people like, let us know if you like it or not.")
        else:
            print("Chocolate is mainly for kids, but you do you.")
    else:
        print("Here is you eclair, enjoy your day.")

# The Cheesecake Factory
else:
    print("There is a 1 hour wait. Do you want to wait to be seated? ")
    print("1. Wait the 1 hour")
    print("2. Choose a different restaurant")
    choice = int(input("What do you choose?: "))
    if(choice == 1):
        print("We apologize for the inconvience the restaurant is now closed and is not taking any more guests!")
        print("Not the birthday dinner you were expecting to have :(")
    elif(choice == 2):
        print("You decided to go to Olive Garden.")
        print("They even gave you free deserts for the whole family and you had excellent service :)")