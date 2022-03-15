from boardmodel import *
from ai import *


def display():
    print("score: ", getScore())
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
# display()
# gameover = False
# while not gameover:
#     print(getBestMove(deepcopy(board), 4))
    
#     # move = input("pick a direction: ")
#     board = move(deepcopy(board), getBestMove(deepcopy(board), 4))
#     validinput = True

#     if move == 'd':
#         board = mergeboardright(board)
#     elif move == 'w':
#         board = mergeboardup(board)
#     elif move == 'a':
#         board = mergeboardleft(board)
#     elif move == 's':
#         board = mergeboarddown(board)
#     else:
#         validinput = False
#     if not validinput:
#         print ("try again")
#     else:
#         if won():
#             display()
#             print("congrats")
#             gameover = True
#         else:
#             addnewvalue()
#             display()

def automate (board):
    gameover = False
    while not gameover:
        board = move(board, getBestMove(board, 4))
        if won():
            display()
            print("congrats")
            gameover = True
        else:
            addnewvalue()
            display()
        display()
automate(board)