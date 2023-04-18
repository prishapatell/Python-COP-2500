# Prisha Patel
# If Statements
# COP 2500 001
# Sep 2 2022

lemon = int(input("How man lemons?\n"))
water = int(input("How many ounces of water?\n"))
sugar = int(input("How many units of sugar?\n"))

# 1 unit of sugar - 2 lemons - 4 oz of water

c_lemon = lemon // 2
c_water = water // 4
c_sugar = sugar

# make sure when if statements, the tabs are properly indented otherwise you will recieve a lot of syntax error
if(c_lemon < c_water):

    if(c_lemon < c_sugar):
        print("Lemons limit the amount of lemonade we made")
        print("We can only make", c_lemon, "cups")
    else: # lemons < water, sugar < lemons  sugar < lemons < water
        print("Sugar limits the amount of lemonade we can make")
        print("We can only make", c_sugar, "cups")
else: # water < lemons

    if(c_water < sugar):
         print("Water limits the amount of lemonade we can make.")
         print("We can only make", c_water,"cups")
    else:
        print("Sugar limits the amount of lemonade we can make")
        print("We can only make", c_sugar, "cups")
