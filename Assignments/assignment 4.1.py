# Prisha Patel
# COP 2500 0001
# Assignment 4.1
# November 4, 2022

print("Welcome to class registration!")

course = ""
course_list = []

def student_list(course_list, course):
    if (len(course_list) < 5):
        choice = input("What courses would you like to add?\n")
        choice = choice.split(",")
        course_list += choice
        print("You have registered in the following courses:")
        for i in range(len(course_list)):
            course_list[i] = course_list[i].strip().title()
            print((i+1), ". ", course_list[i], sep="")
        return course_list

def remove(course_list):
    if (len(course_list) > 5):
        remove_list = input("You have registered for too many courses. What would you like to drop?\n")
        remove_list = remove_list.split(",")
        for i in range(len(remove_list)):
            remove_list[i] = remove_list[i].strip().title()
        for course in remove_list:
            if course in course_list:
                course_list.remove(course)
            else:
                print("Invalid choice. What would you like to drop?\n")
        return course_list

while (len(course_list) != 5):
        student_list(course_list, course)
        remove(course_list)
print("Done!")