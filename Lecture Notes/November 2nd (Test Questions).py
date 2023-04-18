# Prisha Patel
# COP 2500
# November 2, 2022
# Test Questions

def q1(x,y):
    if(x < 5):
        return x+y # return always end
    if(y > 5):
        return x-y
    return x*y
# Question what is returned when the following functions are called:
# a. q1(3,5) = 8
# x = 3
# y = 5
# b. q1(3,10) = 13
# c. q1(10,10) = 0
# d. q1(10,3) = 30
# e. q1(5,5) = 25

def q2(x,y):
    if(x > y):
        y = x+1
        x = x*2
    else:
        y = 0
    return x + y
# Question what is returned then the following function is called:
# a. q210,2) = 31
# x = 10 -> 20 
# y = 2 -> 11 
# b. q2(5,5) = 5
# x = 5 
# y = 5 -> 0
# c. q2(10,12) = 10
# x = 10
# y = 12 -> 0

def q3(a,b,c):
    if(a > b):
        b = q2(a,c)
    return a+b+c
# a. q3(5,3,2) = 23
    # a = 5
    # b = 3 -> 16
    # c = 2
        # q2(5,2) = 16
        # x = 5 -> 10
        # y = 2 -> 6
# b. q3(5,3,10) = 20
    # a = 5
    # b = 3 -> 5
    # c = 10
        # q2(5,10) = 5
        # x = 5
        # y = 10 -> 0
# c. q3(5,8,2) = 15

def q4(a,b):
    while(a < b):
        a = a+1
        b = b-1
    return a
# a. q4(4,8) = 6
    # a = 4 -> 5 -> 6
    # b = 8 -> 7 -> 6
# b. q4(4,4) = 4
    # a = 4
    # b = 4
# c. q4(8,4) = 8
    # a = 8
    # b = 4
# d. q4(4,7) = 6
    # a = 4 -> 5 -> 6
    # b = 7 -> 6 -> 5