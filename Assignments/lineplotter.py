# Prisha Patel
# lineplotter
# COP 2500 0001
# October 1, 2022

slope = float(input("Enter the slope: "))
intercept = float(input("Enter the intercept: "))
print("Line y = " ,slope,"x +",intercept,": ")

for num in range(0,10):
    total = (slope * num) + intercept
    print("At x =" ,num, ", y = ",total,)

for x in range(1,6):
    ten = pow(10, x)
    total_tens = (slope * ten) + intercept
    print("At x =", ten, "y = ", total_tens,)
