# Prisha Patel
# COP 2500 0001
# Dictionaries
# November 14, 2022

# dictionaries : key words and {}
credit_hours = {'cop2500':3}
course = input("What course would you like to add or lookup?\n")
while (course.lower() != "exit"):
    course = course.lower().strip()
    if course == "lookup":
        for key in credit_hours.key():
            print(key,"-",credit_hours.keys())
    elif course in credit_hours.keys():
        print(course, "is worth", credit_hours[course],"credits")
    else:
        print(course, "is not in the dictionary")
        credit = int(input("How many credits is "+course+"?\n")) # ++ is used to join two strings
        credit_hours[course] = credit
    course = input("What course would you like to add or lookup?\n")
