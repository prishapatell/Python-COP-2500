# Prisha Patel
# COP 2500 0001
# Lists
# October 24th, 2022

# To printout list
example = [1,2,3,4,5]
answer = 0

for index in range(4):
    answer = answer + example[index]
print(answer)

for i in range(len(example)):
    answer = answer + example[index]
print(answer)

for index in range (len(example)):
    print(index+1, "-", example[index])
    print(index)

for index in range (len(example)):
    print(index+1, "-", example[index], sep="", end=" ")


master_list = []
master_list_2 = []


line = input("Enter Names\n")
print(line)
line = line.split(",")
print(line)

for index in range(len(line)):
    line[index] = line[index].strip()

for index in range (len(line)):
    print((index+1),"-", line[index])

# To remove something from a list
value = int(input("Which value would you like to remove?\n"))
value = value - 1

line.pop(value)
for index in range (len(line)):
    print((index+1),"-", line[index])

# Works if you don't care about duplicates
    master_list = master_list + line
# Check to see if that value is in the list
for index in range(len(line)):
    if not line[index] in master_list_2:
        master_list_2.append(line[index])

names = input("Enter banned names")
names = names.split(",")
for index in range(len(names)):
    names[index] = names[index].strip()
    if names[index] in master_list:
        master_list.remove(names[index])
    if names[index] in master_list_2:
        master_list_2.remove(names[index])

print("Master List")
for index in range(len(master_list)):
    print((index+1),"-",master_list[index])
print("Master List 2")
for index in range(len(master_list_2)):
    print((index+1),"-",master_list_2[index])