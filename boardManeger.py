from boardmodel import *
from ai import *


def display():
    print("Score: ", getScore())
    #Finding out which value is the largest
    largest = board[0][0]
    for row in board:
        for element in row:
            if element > largest:
                largest = element
    
    #Setting the max number of spaces needed to the length of the largest value
    numspaces = len(str(largest))

    for row in board: #display a vertical line in front and in between each number for clarity
        currentrow = "|"
        for element in row:
            if element == 0:
                currentrow +=" "*numspaces + "|" #fitting the empty spaces to the largest number's number of spaces needed
            else:
                    currentrow +=(" "*(numspaces - len(str(element)))) + str(element) + "|" #fitting the numbered spaces to the largest number's number of spaces needed
        print(currentrow)
    print()

print("welcome to 2048)")

def automate (board):
    gameover = False
    while not gameover:
        availableCells =getAvailableCells(board)
        depth = 0
        if len(availableCells) > 5 :
            depth = 5
        else:
            depth = 6
        board = move(board, getBestMove(board, depth), "real")
        if won():
            display()
            print("congrats")
            gameover = True
        else:
            addnewvalue()
            display()
automate(board)