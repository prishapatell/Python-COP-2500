# Prisha Patel 
# COP 2500 0001
# Functions
# October 12, 2022

# Question 6 on the Midterm
def change_list(quote):
    for index in range (len(quote)):
        if (index % 2 == 0):
            quote[index] = quote[index].upper()
        else:
            quote[index] = quote[index].lower()
        return quote

words = ["general","Kenobi", "you", "aRe", "a", "boLd", "one"]
answer = change_list(words)
print(answer)


def who_is_happy(season):
    if(season <= 4):
        return "Kyle"
    if(season == 13 or season >= 26):
        return "Juila"
    return "Neither"
# You can also use this way, it works perfectly fine
    #if(season <= 4):
        #return "Kyle"
    #elif(season == 13 or season >= 26):
        #return "Juila"
    #else:
        #return "Neither"

answer = who_is_happy(26)
print(answer)

def q1(x ,y):
    z = 0
    while (x > y):
        x -= 2
        y += 1
        z += 1
    return z
# x = 10 -> 8 -> 6
# y = 5 -> 6 -> 7
# z = 0 -> 1 -> 2
answer = q1(10,5)
print(answer)

def q2(x ,y):
    z = 0
    while (x > y):
        x -= 2
        y += 1
        z += 1
        return z
    return 5    # when we use return keys we only get one thing back
answer = q2(10,5)
print(answer)
answer = q2(4,5)
print(answer)

value1 = int(input("Input a number:\n"))
value2 = int(input("Input a number:\n"))
answer = q1(value1, value2)
print(answer)

answer = q1(int(input("Input a number:\n")), int(input("Input a number:\n")))


