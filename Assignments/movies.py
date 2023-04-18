# Prisha Patel
# Movies
# COP 2500 0001
# September 16, 2022

# small monster collectors is $9.50
# individiual ticket is $12.0
# if more than 25 people the group rate will go down to $7.25 per person

small_mosters_collectors = 9.50
individiual_person = 12.0
group_rate = 7.25

moviegoers = int(input("Enter the number of moviegoers: "))

if(moviegoers < 25):
    price = ((moviegoers - 1) * individiual_person + small_mosters_collectors)
    print( "The total ticket price is $ ", price,)
elif(moviegoers > 25):
    price = (moviegoers * group_rate)
    print( "The total ticket price is $ ", price,)
