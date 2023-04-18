# Prisha Patel
# COP 2500 0001
# Files Input & Ouput
# October 17, 2022

# We are looking for comma deliminated for cvs files for excel files

# Read, Write, Append, Create
# Most Important ones today: Read and Write
number = 10

fileWrite = open("example.txt", "w")

fileWrite.write("Hello Class\n")
fileWrite.write("How are you\n")
# You cannot put a string and interger here
#fileWrite.write("There are", + str(number) + "people here")

fileWrite.close()

fileInput = open("input.txt")
print(fileInput)
number = fileInput.readlines()

for num in range(number):
    temp= int(fileInput.readline()) + 1
    total += (temp)

print(total)
fileInput.close()


fileInput = open("input.txt", "r")
print(fileInput)
number = fileInput.readlines()

for num in range(number):
    temp= int(fileInput.readline())
    if(temp %2 == 0):
        total += temp
    total += (temp)

print(total)
fileInput.close()
