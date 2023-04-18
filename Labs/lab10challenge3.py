# Prisha Patel
# COP 2500 0001
# lab 10 challenge 3
# November 29, 2022

import csv

course_list =  []

with open ("Lab10.csv","r") as f:
    reader = csv.reader(f, delimiter = "\t")
    for i, line in enumerate (reader):
        line_items = line[0].split(",")
        #print(line_items)
        temp_dict = {
            "course_code" : line_items [0],
            "course_name" : line_items [1],
            "credit_hours" : line_items [2],
            "teacher" : line_items [3],
            "grade" : line_items [4],
            }
        course_list.append(temp_dict)
    print(course_list)
