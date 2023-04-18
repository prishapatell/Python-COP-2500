# Prisha Patel
# Lab 1 Challenge 3
# COP 2500 0001
# Aug 30, 2022

# Input
pizza = int(input("How many pizzas would you like to order?\n"))
people = int(input("How many people are you feeding?\n"))

totalperpizza = 8

totalslices = (totalperpizza*pizza)

slicesperperson = int(totalslices/people)



print("You will have", slicesperperson, "slices per person.")
