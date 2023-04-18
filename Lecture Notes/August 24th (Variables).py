# Prisha Patel
# Day 2 Variables
# COP 2500 0001
# Aug 24, 2022

age = 21
# = is not an equal sign but rather a set to sign
print("age", age)
# anything in "" is strains, hence in a green color to show it
money =7.99
# the way you do math on a number vs a strain is different
print("$", money)
print("$",money, sep="----")
# sep 
print("$", money, sep="")
# arithmetic function include: +, -, *, /, //, %
# + is addition
# - is subtraction
# * is multiply
# /is division
# // is integer division, division without decimals
# % is called modulus, meaning remainder

age = age + 5
print("Age:", age)

money = money * 1.065
# money * 1.065 will actually run without error so BE CAREFUL
print("Money:", money)
print("Money:", money, sep="") # this is different because there is no space between the : and the number result

age += 5 #+= has the same function as age = age + 5
print("AGE:", age)

print(9 / 5)
print(9 // 5)
