# Prisha Patel
# COP 2500 0001
# Tic Tac Toe Game
# October 26, 2022

def print_board(board):
    print("0 1 2")
    print(" ")
    for row in range(3):
        print(row,end=":")
        for col in range(3):
            if (col == 2):
                print(board[row][col])
            else:
                print(board[row][col],end=" ")
        print("-+-+-+")

board = [5,5,5]
board = [[0,0,0],[0,0,0],[0,0,0]]
# row major order
# the row comes first then the column
board = [[0,0,0],
         [0,0,0],
         [0,0,0]]
print(board[1][0])  #prints 3

turn = 0

while(turn < 9):
    if(turn % 2 == 0):
        print("It is Shaawn's Turn")
    else:
        print("It is Kyle's Turn")

    for row in range(3):
        for col in range(3):
            print(board[row][col],end=" ")
        print()

    x,y = map(int,input("What position would you like to go in?").split())
    if(turn % 2 == 0 and board[y][x] == 0):
        board[y][x] = 1
        turn += 1
    elif(turn % 2 == 1 and board[y][x] == 0):
        board[y][x] = 2
        turn += 1
# Check to see if we can win
    for i in range(3):
        if(board[0][i] == 1 and board[1][i] == 1 and board[2][i] == 1):
            print("Shaawn Wins!")
            turn = 10
        elif(board[i][0] == 1 and board[i][0] == 1 and board[i][2] == 1):
            print("Shaawn Wins!")
            turn = 10
        elif(board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2):
            print("Kyle Wins!")
            turn = 10
        elif(board[0][i] == 2 and board[1][i] == 2 and board[2][i] == 2):
            print("Kyle Wins!")
            turn = 10
        
    if(board[0][0] == 1 and board[1][1] == 1 and board[2][2] == 1):
         print("Shaawn Wins!")
    if(board[2][0] == 1 and board[1][1] == 1 and board[0][2] == 1):
        print("Shaawn Wins!")
    if(board[0][0] == 2 and board[1][1] == 2 and board[2][2] == 2):
        print("Kyle Wins!")
    if(board[2][0] == 2 and board[1][1] == 2 and board[0][2] == 2):
        print("Kyle Wins!")
print_board(board)
