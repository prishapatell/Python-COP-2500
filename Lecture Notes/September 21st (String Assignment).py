# Prisha Patel
# String Assignment
# COP 2500
# September 21, 2022

print("Would you like to play a game?")
response = input()

response = response.lower()
response = response.strip()

response = response.lower().strip()

if response == "yes":
    print("How about a good game of chess?")
    response = input()
    response = response.lower().strip()
    while(response != "yes"):
        print("Why not? Let's play!")
        response = input()
    print("We played chess")
elif response == "global themanucler war":
    pass
