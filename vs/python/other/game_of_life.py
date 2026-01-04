#def nextgen decides whether a piece is born, lives, dies. changes piece[1]
#def endday kills or alives a piece. uses piece[0]
#def neighboors says how many neighboors a piece has. uses board from showboard()
#def showboard turns the board into a readable format
#printboard prints the board with formatting
#fullboard = lives ..... board1 = board 

import time as t

def showboard(fullboard):
    result = []
    for n in range(0, 10):
        for i in range(0, 10):
            result.append(fullboard[n][i][0])
    global board
    board = []
    for n in range(1, 11):
        board.append(result[(n-1)*10:n*10])

def neighboors(board1, index):
    count = 0
    if index[0] == 0:
        #top row
        if index[1] == 0:
            #topleft piece
            if board1[index[0]+1][index[1]+1] == 1:
                count += 1
            if board1[index[0]][index[1]+1] == 1:
                count += 1
            if board1[index[0]+1][index[1]] == 1:
                count += 1
        elif index[1] == 9:
            #topright piece
            if board1[index[0]+1][index[1]-1] == 1:
                count += 1
            if board1[index[0]+1][index[1]] == 1:
                count += 1
            if board1[index[0]][index[1]-1] == 1:
                count += 1
        else:
            if board1[index[0]+1][index[1]-1] == 1:
                count += 1
            if board1[index[0]+1][index[1]+1] == 1:
                count += 1
            if board1[index[0]][index[1]+1] == 1:
                count += 1
            if board1[index[0]+1][index[1]] == 1:
                count += 1
            if board1[index[0]][index[1]-1] == 1:
                count += 1
    elif index[0] == 9:
        #bottom row
        if index[1] == 0:
            #bottomleft piece
            if board1[index[0]-1][index[1]] == 1:
                count += 1
            if board1[index[0]][index[1]+1] == 1:
                count += 1
            if board1[index[0]-1][index[1]+1] == 1:
                count += 1
        elif index[1] == 9:
            #bottomright piece
            if board1[index[0]][index[1]-1] == 1:
                count += 1
            if board1[index[0]-1][index[1]] == 1:
                count += 1
            if board1[index[0]-1][index[1]-1] == 1:
                count += 1
        else:
            if board1[index[0]][index[1]-1] == 1:
                count += 1
            if board1[index[0]-1][index[1]] == 1:
                count += 1
            if board1[index[0]][index[1]+1] == 1:
                count += 1
            if board1[index[0]-1][index[1]-1] == 1:
                count += 1
            if board1[index[0]-1][index[1]+1] == 1:
                count += 1
    elif index[1] == 0:
        #left row without corner pieces
        if board1[index[0]-1][index[1]] == 1:
            count += 1
        if board1[index[0]][index[1]+1] == 1:
            count += 1
        if board1[index[0]+1][index[1]] == 1:
            count += 1
        if board1[index[0]-1][index[1]+1] == 1:
            count += 1
        if board1[index[0]+1][index[1]+1] == 1:
            count += 1
    elif index[1] == 9:
        #right row without corner pieces
        if board1[index[0]-1][index[1]-1] == 1:
            count += 1
        if board1[index[0]+1][index[1]-1] == 1:
            count += 1 
        if board1[index[0]-1][index[1]] == 1:
            count += 1
        if board1[index[0]+1][index[1]] == 1:
            count += 1
        if board1[index[0]][index[1]-1] == 1:
            count += 1
    else:
        #other pieces
        #checking diagonals
        if board1[index[0]-1][index[1]-1] == 1:#topleft
            count += 1
        if board1[index[0]-1][index[1]+1] == 1:#topright
            count += 1
        if board1[index[0]+1][index[1]-1] == 1:#bottomleft
            count += 1
        if board1[index[0]+1][index[1]+1] == 1:#bottomright
            count += 1
        #checking verticals & horizontals
        if board1[index[0]-1][index[1]] == 1:#top
            count += 1
        if board1[index[0]][index[1]+1] == 1:#right
            count += 1
        if board1[index[0]+1][index[1]] == 1:#bottom
            count += 1
        if board1[index[0]][index[1]-1] == 1:#left
            count += 1
    
    return count

def nextgen(fullboard, board1):
    for n in range(0, 10):
        for i in range(0, 10):
            neighboornum = neighboors(board1, [n, i])
            if neighboornum <= 1:
                fullboard[n][i][1] = 0
            elif neighboornum in (2,3):
                fullboard[n][i][1] = 1
            elif neighboornum >= 4:
                fullboard[n][i][1] = 0
    return fullboard

def newworld(fullboard):
    for n in range(0, 10):
        for i in range(0, 10):
            if fullboard[n][i][1] == 0:
                fullboard[n][i][0] = 0
            else:
                fullboard[n][i][0] = 1
    return fullboard

def printboard(board1):
    for n in range(0, 9):
        print(' ', board1[n][0], '│', board1[n][1], '│', board1[n][2], '│', board1[n][3], '│', board1[n][4], '│', board1[n][5], '│', board1[n][6], '│', board1[n][7], '│', board1[n][8], '│', board1[n][9])
        print(' ───┼───┼───┼───┼───┼───┼───┼───┼───┼─── ')
    print(' ', board1[n][0], '│', board1[n][1], '│', board1[n][2], '│', board1[n][3], '│', board1[n][4], '│', board1[n][5], '│', board1[n][6], '│', board1[n][7], '│', board1[n][8], '│', board1[n][9])

def calcpopulation(board1):
    pop = 0
    for n in board1:
        pop += n.count(1)
    return pop

lives = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [1, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [1, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],
         [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0],],]

for generation in range(1, 101):#num of generations
    t.sleep(0.8)
    showboard(lives)
    printboard(board)
    lives = nextgen(lives, board)
    showboard(lives)
    lives = newworld(lives)
    population = calcpopulation(board)
    print(f'\t\t\t\t\t\tgeneration:{generation}\t\tpopulation:{population}')