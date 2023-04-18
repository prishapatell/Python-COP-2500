# Prisha Patel
# Input/Variable Types
# COP 2500.001
# Aug 26, 2022

# Types of Data
    # - Integers    int
    # - Floats      float
    # - Strings     str

print(1+2)
print("1"+"2")
# When we add strings, we join them together

one = "1"
two = "2"

print(one + two)

print( int(one) + int(two) )
print( int(one) + int(two) + 1)

# Input
lemonade = int(input("How many cups of lemonade would you like?\n"))
cost = float(input("How much does it cost?\n"))
name= str(input("What is the name of your order?\n"))

total = lemonade * cost

print(name, "your order of", lemonade, "cups of lemonade is ready")
print("That will be $", total,  sep="")
# getting into the habit of attaching string to string
# Assignment 1.1 is in integers not in float
