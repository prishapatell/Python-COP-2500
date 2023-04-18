#Prisha Patel
#October 31, 2022
#COP2500
#2D Lists

#Takes in a row (or a single list) and add all the numbers together
def sum_row(row):
    answer = 0
    for i in range(len(row)):
        answer+=row[i]
    return answer

#Takes in a 2D list and returns a list that has a sum of each row
#Very Important to remember
def sum_each_row(matrix):
    answer = []
    
    for r in range(len(matrix)):
        total = sum_row(matrix[r])
        answer.append(total)
    return answer

def sum_max(matrix):
    max_list = []
    for r in range(len(matrix)):
        a = max(matrix[r])
        max_list.append(a)
        #print(max_list)
    return sum_row(max_list)

def drop_grade(grades):
    if(len(grades) == 0):
       return grades
    grades = grades.copy()
    lowest = min(grades)
    grades.remove(lowest)
    return grades


def class_drop(gradebook, how):
    gb = gradebook.copy()
    for row in range(len(gb)):
        for i in range(how):
            gb[row] = drop_grade(gb[row])
    return gb

def main():
    #                 96            162             58          9 
    test_list = [[10, 55, 31], [13, 85, 64], [33, 3, 4, 17], [8, 1]]
    a = sum_row(test_list[1])
    print(a)

    b = sum_each_row(test_list)
    print(b)
    
    c = sum_max(test_list)
    print(c)

    d = class_drop(test_list, 1)
    print(d)

    d = class_drop(test_list, 2)
    print(d)

    d = class_drop(test_list, 3)
    print(d)

    d = class_drop(test_list, 1)
    print(d)
main()