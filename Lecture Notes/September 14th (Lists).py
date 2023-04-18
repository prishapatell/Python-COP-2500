# Prisha Patel
# Lists
# COP 2500 0001
# September 14, 2022

# [] - creates a list
store = []

# add things to the end of the list
store.append("Oreos")
store.append("Cookies")
store.append("Publix Sub")
store.append("Chips")
store.append("Salsa")
print(store)

# inserts into a location
store.insert(0, "Bananas") #0 in the beginning is an indicator where to put the item in the list
store.insert(2, "Bananas")
print(store)

# remove something, the first one will only be removed from the list
if "Bananas" in store:
    store.remove("Bananas")
if "Oranges" in store:
    store.remove("Oranges")
print(store)


# while loop will remove all bananas
while "Bananas" in store:
    store.remove("Bananas")

# delete at a position, you have to go one down when in range
store.pop(0)
print(store)


# how to get the size of the list
value =len(store)  #len - lenght
print(value)

# sort the list
store.sort()
print(store)

#when sorting be careful of lowercase and uppercase, based on the ascii chart
# uppercase alphabetical is different than lowercase alphabetical
