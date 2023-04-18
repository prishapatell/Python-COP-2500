# Prisha Patel
# Left Right Game
# COP 2500 0001
# September 14, 2022

import random

board = []

for num in range(4):
    board.append(random.randint(1,9))
    board.append(random.randint(1,9))

turn = 0
kyles_score = 0
class_score = 0

while(len(board)!= 0):
    print("It's player", (turn%2+1),"turn")
    for num in range(len(board)):
        print(board[num], end="")
    print()
    print("Kyle's Score:", kyles_score)
    print("Class's Score:", class_score)

    choice = input("Left or Right:\n")

    if(choice == "Left"):
        if(turn%2 == 0):
            kyles_score += board[0]
            board.pop(0)
            turn+=1
        else:
            class_score += board[0]
            board.pop(0)
            turn+=1
    if(choice == "Right"):
        if(turn%2 == 0):
            kyles_score += board[-1]
            board.pop(-1)
            turn+=1
        else:
            class_score += board[-1]
            board.pop(-1)
            turn+=1

print("Game Over")
if(kyles_score > class_score):
    print("Kyle won!")
    print("By", kyles_score - class_score)
elif(kyles_score == class_score):
    print("We tie... Thats Fine")
else:
    print("Never will happen")
