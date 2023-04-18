# Prisha Patel
# COP 2500 0001
# Data Verification
# October 19, 2022

#5 Steve as a and b

line = input("Enter a number and a name").split()
a = int(line[0])
b = line[1]

print(a+1)
print(b)

#3 5 save these as a and b
a, b = map(int, input("Enter a and b").split())

print(a,b)

line = input("Enter a and b")
line = line.split()
a, b = map(int, line)
print(a,b)
print(line)

c = int(line[0])
d = int(line[1])

print(c,b, "=", c + b)
#Enter  a number between 1 - 100
number = int(input("Enter a number between 1 and 100"))

while (number < 1 or number > 100):
    print("You entered an invalid number.")
    number = int(input("Enter a number between 1 and 100"))

print("Done.\n")


#Check to see if it is a number
number = input("Enter a number between 1 and 100")

#Checks to see if it's a valid number
while(not number.isdigit() or float(number) < 1 or float(number) > 100):
    print("You entered an invalid number.")
    number = input("Enter a number between 1 and 100")


print("Done.\n")

#Enter a username
username = input("Enter a username")

while(not username.isalnum()):
    print("Your username can only have numbers and letters")
    username = input("Enter a username")

print("Done.\n")