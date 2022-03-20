from copy import deepcopy
from boardmodel import  getAvailableCells, move

min_value = 0.1 #setting the value to 0.1 instead of 0 in order to be able to notice whether or not the 
#new score is different from the min score later


def getBestMove(board, depth): # making a copy of the board as the next move, if it doesn't change the board continue or else apply the expectimax func to it
    MoveScore = min_value
    bestMove = 0
    for moveNum in range(4):
        newBoard = deepcopy(board)
        nextLevel = move(deepcopy(newBoard), moveNum, "belive")
        if(newBoard == nextLevel):
            continue
        #call up the expectimax function to decide whether the next move is best in case of change to the board
        newScore = expectiMax(deepcopy(nextLevel), depth - 1, "board")
        if newScore > MoveScore :
            bestMove = moveNum
            MoveScore = newScore
    print("newMoveScore: ", MoveScore, "move: ", bestMove)
    return bestMove

def expectiMax(board, depth, agent): 

    if depth == 0: 
        return calculateScore(board)
    elif agent == "player" :
        playerScore = min_value        
        for moveNum in range(4):
            newBoard = deepcopy(board)
            nextLevel = move(deepcopy(newBoard), moveNum, "belive")
            if nextLevel == newBoard:
                continue

            newScore = expectiMax(deepcopy(nextLevel), depth - 1, "board")

            if newScore > playerScore:
                playerScore=newScore
        return playerScore
    
    elif agent == "board":
        boardScore = 0
        availableCells = getAvailableCells(board)
        for cellIndex in availableCells:
            newBoard = deepcopy(board) 
            newBoard[cellIndex[0]][cellIndex[1]] = 2
            newScore = expectiMax(deepcopy(newBoard), depth-1, "player")
            if not newScore == min_value:
                boardScore =boardScore+(0.9*newScore)

            
            costumeBoard = deepcopy(board)
            costumeBoard[cellIndex[0]][cellIndex[1]] = 4
            newScore = expectiMax(deepcopy(costumeBoard), depth-1, "player")

            if not newScore == min_value:
                boardScore =boardScore+(0.1*newScore)

            # boardScore = boardScore/len(availableCells)
        return boardScore

#heuristics function rewarding the agent to keep the highest number in a corner and adding penalty if it doesn't

def calculateScore(board):
    priority =     [[ 14,  9,  8,  4],
                    [ 10,  8,  5,  4],
                    [ 2,  1,  1, 0],
                    [ 0,  0, -1, -2]]
 

    gameScore = 0
    
    for i,_ in enumerate(board):
        for j,_ in enumerate(board[i]):
            if board[i][j] > 0:
                gameScore += priority[i][j] * board[i][j] * board[i][j]
    
    penalty = 0
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    for i,_ in enumerate(board):
        for j,_ in enumerate(board[i]):
            if board[i][j] > 0:
                for k in range(4):
                    pos = [ j + directions[k][0],  i+ directions[k][1]]
                    if withinBounds(pos): 
                        neighbour = board[pos[0]][pos[1]]
                        if neighbour > 0 :
                            penalty += abs((neighbour - board[i][j]) * 1)
    return gameScore - penalty

def withinBounds (pos):
    return pos[0] >= 0 and pos[0] < 4 and pos[1] >= 0 and pos[1] < 4