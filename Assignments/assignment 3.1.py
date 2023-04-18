# Prisha Patel
# COP 2500 0001
# Assignment 3.1
# October 28, 2022

print("Welcome to class registration!")

course = ""
course_list = []
number = 0

course = input("Enter a course code?\n")

while course != "EXIT": 
    print("You have registered in the following courses:")
    course_list.append(course)

    if course != "EXIT":
        for i in range(len(course_list)):
            print((i+1),".",course_list[i])

        if len(course_list) > 5:          
            print("You have registered for too many courses. Please pick one to delete.")
            number = int(input("Enter a number between 1 and 6.\n"))
            
            while number < 1 or number > 6:
                print("Invalid choice. Choose again")
                number = int(input("Enter a number between 1 and 6.\n"))

            course_list.pop(number - 1)
    
    course = input("Enter a course code?\n")
print("Goodbye")
