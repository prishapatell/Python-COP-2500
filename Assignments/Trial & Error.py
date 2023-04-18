# Prisha Patel

print("Welcome to the flight calculator!")
flight_base = float(input("What is the base fare: \n"))
adults = int(input("How many adults are attending?:\n"))
children = int(input("How many children are attending?:\n"))
adult_t = float(adults*flight_base)
children_d = float(flight_base*0.90)
children_t = float(children*children_d)
total = adult_t + children_t
print("Receipt")
print("%.2f"%adults,"Adults @", "%.2f"%flight_base,"\t$","%.2f"%adult_t)
print("%.2f"%children,"Children @", "%.2f"%children_d,"\t$","%.2f"%children_t)
print("Total\t\t\t$",total)