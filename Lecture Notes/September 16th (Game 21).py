# Prisha Patel
# Game 21
# COP 2500 0001
# September 16, 2022

import random

hand = []
dealer_hand = []
deck = []

for card in range(1,4):
    for num in range(4):
        if(card < 10):
            deck.append(card)
        else:
            deck.append(10)


score = 0
dealer = 0

card = random.randint(0, len(deck))
print(card)
dealer.append(deck[card])
dealer_score = deck[card]
deckpop(index)

card = random.randint(0, len(deck))
hand.append(deck[card])
score = deck[card]
deck.pop(card)

card = random.randint(1,13)
if(card > 10):
    card = 10

card = random.randint(1,13)
if(card > 10):
    card = 10

hand.append(card)
score = score + card

print(hand)
print(score)

# Player's Turn
# Hit means another card
# Stay is your done with your round
stay = False

while(stay == False):
    print("Your hand", hand)
    print("Dealer's hand", dealer)

    choice = int(input("Hit or Stay?\n"))

    if(choice == "Hit"):
        card = random.randint(1,13)
        if(card > 10):
            card = 10
        hand.append(card)
        score = score + card
    elif(choice == "Stay"):
        stay = True

# Dealer's Turn
# Dealer is automatic
while(dealer_score < 16):
     card = random.randint(1,13)
     if(card > 10):
        card = 10
     dealer.append(card)
     dealer_score = dealer_score + card
# End of Dealer's Turn


print("Your hand",hand)
print("Dealer's hand",dealer)

# Who wins
if(score > 21):
    print("You went over 21, you lose.")
elif(dealer_score > 21):
    print("Dealer went over 21 you win!")
elif(dealer_score < score):
    print("You win!")
else:
    print("You lose")






