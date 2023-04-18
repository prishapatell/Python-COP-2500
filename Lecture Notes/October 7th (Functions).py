# Prisha Patel
# Functions - Store
# COP 2500 0001
# Oct 7, 2022
# Go to CodingBat.com to do alot of python practice DO IT

def menu():
    print("1. Buy Jersey")
    print("2. Sell Jersey")
    print("3. Check Inventory")
    print("4. Exit")
    choice = int(input("What is your choice?\n"))
    return choice

def buy_jersey(total_money,items,cost):
    total_cost = items * cost
    if(total_cost <= total_money):
        return total_money - total_cost
    else:
        return -1

def main():
    print("Welcome to the space game store")
    jersey = 20
    money = 600
    option = menu()

    while (option != 4):
        if (option == 1):
            js = int(input("How many jerseys would you like to buy?\n"))
            cost = float(input("How much do they cost?\n"))
            new_balance = buy_jersey(money,js,cost)
            if (new_balance == -1):
                print("We do not have this type of money")
            else:
                jersey += js
                money = new_balance
                print("You were able to buy", js, "jerseys.")
                
        if (option == 2):
            pass
        if (option == 3):
            print("Jersey Total:", jersey)
            print("Money $", money)

main() # putting this is what actually makes it print in the termial
