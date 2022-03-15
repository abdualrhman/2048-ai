from copy import copy
import random
# from ai import expectiMax
score = 0
boardsize =4
board=[]
def getScore ():
    return score

def display():
    print("score: ", score)
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


def insertCell (index, val):
    board[index[0]][index[1]] = val

def mergeonerowleft(row): #funtion to merge one row left
    global score
    for j in range(boardsize - 1): #repeat the moving left operation 3 times
        for i in range (boardsize - 1, 0, -1): #moving everything as far left as possible
            if row[i-1] ==0:
                row[i-1] = row[i]
                row[i] = 0
    # Merging to the left
    for i in range (boardsize - 1):
        if row[i] == row[i+1]:
            row[i] *=2
            score =  score +row[i]
            row[i+1] = 0
    #move evrything to the left again
    for i in range (boardsize-1,0,-1):
        if row[i-1] == 0:
            row[i-1] = row[i]
            row[i] = 0
        return row
#function to merge the whole board left
def mergeboardleft(currentboard):
    for i in range (boardsize):
        currentboard[i] = mergeonerowleft(currentboard[i])
    return currentboard

def getAvailableCells(board):
    availableCells=[]
    for i, _ in enumerate(board):
        for j, _ in enumerate(board[i]):
            if board[i][j] == 0:
               availableCells.append([i, j])
    return  availableCells

#function to reverse the order of one row
def reverse(row):
    new = []
    for i in range (boardsize-1,-1,-1):
        new.append(row[i])
    return new

def mergeboardright(currentboard): #funtion to merge the whole board right
    for i in range(boardsize):
        currentboard[i] = reverse(currentboard[i])
        currentboard[i] = mergeonerowleft(currentboard[i])
        currentboard[i] = reverse(currentboard[i])
    return currentboard


#funtion to transpose the whole board
def transpose(currentboard):
    for j in range(boardsize):
        for i in range(j,boardsize):
            if not i==j:
                temp=currentboard[j][i]
                currentboard[j][i] = currentboard[i][j]
                currentboard[i][j] = temp
    return currentboard

def mergeboardup(currentboard):
    currentboard = transpose(currentboard)
    currentboard= mergeboardleft(currentboard)
    currentboard = transpose(currentboard)  
    return currentboard

def mergeboarddown(currentboard):
    currentboard = transpose(currentboard)
    currentboard = mergeboardright(currentboard)
    currentboard =transpose(currentboard)
    return currentboard
    

#function to initialize a 2 or 4 value on the starting board
def picknewvalue():
    if random.randint(1,9) ==1:
        return 4
    else:
        return 2

#function to add a new value to the board on an empty space
def addnewvalue():
    rowNum = random.randint(0,boardsize-1)
    colNum = random.randint(0,boardsize-1)
        #finds an empty spot
    while not board[rowNum][colNum]==0 :
        rowNum = random.randint(0,boardsize-1)
        colNum = random.randint(0,boardsize-1)
        #insert new value in empty spot
    board[rowNum][colNum] = picknewvalue()

def won():
    for row in board:
        if 2048 in row:
            return True
    return False


board= []
for i in range(boardsize):
    row = []
    for j in range(boardsize):
        row.append(0)
    board.append(row)

#selecting 2 random spots with random values (2,4)
numbersNeeded= 2
while numbersNeeded > 0:
    rowNum = random.randint(0,boardsize-1)
    colNum = random.randint(0,boardsize-1)

    if board[rowNum][colNum] == 0:
        board[rowNum][colNum] = picknewvalue()
        numbersNeeded -= 1
# print("welcome to 2048)")
# display()      

def move(newBoard, num):
    if num == 0:
        return mergeboardup(newBoard) 
    elif num == 1:
        return mergeboardright(newBoard) 
    elif num == 2:
        return mergeboarddown(newBoard) 
    elif num == 3:
        return mergeboardleft(newBoard) 



