# Prisha Patel
# COP 2500 0001
# lab9challenge3
# November 8, 2022

def checkCourseGrades(gradeList):
    tempanswer = 0
    for i in range(len(gradeList)-1):
        print(gradeList[i], gradeList[i+1])
        if gradeList[i] < gradeList[i+1]:
            print("Increased")
            tempanswer += 1
    return tempanswer

def main():
    Semester = [ [95, 92, 93, 96, 92],
                 [100, 100], 
                 [70, 80, 90], 
                 [95, 85, 75, 70] ]
    answer = []
    for course in Semester:
        increase = checkCourseGrades(course)
        answer.append(increase)
    print(answer)

main()