# Prisha Patel
# Intro to Strings
# COP 2500 0001
# September 19, 2022

# https://www.w3schools.com/python/python_strings.asp
# https://www.w3schools.com/python/python_strings_methods.asp

name = "Steven"
other = "Stephen"
other2 = "steve"
other3 = "steven"
other4 = "SteVen"

if (name == other3):
    print("Steven is equal to steven")
else:
    print("Steven is not equal to steven")


if (name.lower() == other3):
    print("Steven is equal to steven")
else:
    print("Steven is not equal to steven")

if (name.lower() == other3.lower()):
    print("Steven is equal to steven")
else:
    print("Steven is not equal to steven")

if (name.upper() == other3.upper()):
    print("Steven is equal to steven")
else:
    print("Steven is not equal to steven")


name = name.lower()
print(name)

print(name.lower())
print(name)

# uppercase
print(name.upper())

# get a character out ofthe string
print(name[2])

name ="sTeVeN"
print(name.title())

tagline = "i like rubber DUCKS!"
print(tagline.capitalize())

# strips take out spaces from the left and right before and after the the first and last word but the spaces inbetween words
address = "    4000 Central Florida Blvd    "
print("!", address,"!")

address = address.strip()
print("!", address,"!")

address2 = "Orlando, Florida 32816"

line = address2.split()
print(line)
# it prints out with [] because it is a list

city = line[0]
state = line[1]
zipcode = int(line[2])

print(city)

# substring
print(city[-1])

# colon : is used as "through"
print(city[:2])
# values 2 - 6 not including 6
print(city[2:6])
# character at position 6
print(city[6])

city = city[:-1]
print(city)


































