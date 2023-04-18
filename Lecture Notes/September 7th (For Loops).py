
# Prisha Patel
# For Loops

# COP 2500 001
# September 7, 2022

# Loops 5 times, from 0-4
for count in range (5):
    print(count)

# Loops 7 times, from 0-6
for count in range (7):
    print(count)

# Loop: 9 times, from 1-10
for count in range (1,10):
    print(count)

# NEVER INCLUDES THE ENDING POINT ON LOOPS


number = int(input("Select a value: "))

for count in range(1, number+1):
    print(count)
print("Number:", number)


for count in range(1, number+1,2):
    print(count)


for count in range(1, number+1,3):
    print(count)
