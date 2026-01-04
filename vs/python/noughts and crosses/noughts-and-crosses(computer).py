import random

def displaygrid(grid):
    print(" ", grid[0][0], "│", grid[0][1], "│", grid[0][2]) 
    print(" ───┼───┼───")
    print(" ", grid[1][0], "│", grid[1][1], "│", grid[1][2]) 
    print(" ───┼───┼───")
    print(" ", grid[2][0], "│", grid[2][1], "│", grid[2][2])

def wincheck(grid):
    if grid[0][0] == grid[0][1] == grid[0][2] and grid[0][0] != " ":
        global winner
        winner = grid[0][0]
        return True
    elif grid[0][0] == grid[1][0] == grid[2][0] and grid[0][0] != " ":
        winner = grid[0][0]
        return True
    elif grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != " ":
        winner = grid[0][0]
        return True
    elif grid[2][0] == grid[1][1] == grid[0][2] and grid[2][0] != " ":
        winner = grid[2][0]
        return True
    elif grid[1][0] == grid[1][1] == grid[1][2] and grid[1][0] != " ": 
        winner = grid[1][0]
        return True
    elif grid[2][0] == grid[2][1] == grid[2][2] and grid[2][0] != " ":
        winner = grid[2][0]
        return True
    elif grid[0][1] == grid[1][1] == grid[2][1] and grid[0][1] != " ":
        winner = grid[0][1]
        return True
    elif grid[0][2] == grid[1][2] == grid[2][2] and grid[0][2] != " ":
        winner = grid[0][2]
        return True
    else:
        winner = False
        return False

def off(grid):#offensive
    if grid[0][0] == grid[0][1] and grid[0][0] != " " and grid[0][2] == " " and grid[0][0] == "o":
        global target
        target = [0,2]
        return True
    elif grid[0][0] == grid[0][2] and grid[0][0] != " " and grid[0][1] == " " and grid[0][0] == "o":
        target = [0,1]
        return True
    elif grid[0][1] == grid[0][2] and grid[0][1] != " " and grid[0][0] == " " and grid[0][1] == "o":
        target = [0,0]
        return True
    elif grid[1][0] == grid[1][1] and grid[1][0] != " " and grid[1][2] == " " and grid[1][0] == "o":
        target = [1,2]
        return True
    elif grid[1][0] == grid[1][2] and grid[1][0] != " " and grid[1][1] == " " and grid[1][0] == "o":
        target = [1,1]
        return True
    elif grid[1][1] == grid[1][2] and grid[1][1] != " " and grid[1][0] == " " and grid[1][1] == "o":
        target = [1,0]
        return True
    elif grid[2][0] == grid[2][1] and grid[2][0] != " " and grid[2][2] == " " and grid[2][0] == "o":
        target = [2,2]
        return True
    elif grid[2][0] == grid[2][2] and grid[2][0] != " " and grid[2][1] == " " and grid[2][0] == "o":
        target = [2,1]
        return True
    elif grid[2][1] == grid[2][2] and grid[2][1] != " " and grid[2][0] == " " and grid[2][1] == "o":
        target = [2,0]
        return True
    elif grid[0][0] == grid[2][0] and grid[0][0] != " " and grid[1][0] == " " and grid[0][0] == "o":
        target = [1,0]
        return True
    elif grid[0][0] == grid[1][0] and grid[0][0] != " " and grid[2][0] == " " and grid[0][0] == "o":
        target = [2,0]
        return True
    elif grid[1][0] == grid[2][0] and grid[1][0] != " " and grid[0][0] == " " and grid[1][0] == "o":
        target = [0,0]
        return True
    elif grid[0][1] == grid[1][1] and grid[0][1] != " " and grid[2][1] == " " and grid[0][1] == "o":
        target = [2,1]
        return True
    elif grid[0][1] == grid[2][1] and grid[0][1] != " " and grid[1][1] == " " and grid[0][1] == "o":
        target = [1,1]
        return True
    elif grid[1][1] == grid[2][1] and grid[1][1] != " " and grid[0][1] == " " and grid[1][1] == "o":
        target = [0,1]
        return True
    elif grid[0][2] == grid[1][2] and grid[1][2] != " " and grid[2][2] == " " and grid[0][2] == "o":
        target = [2,2]
        return True
    elif grid[0][2] == grid[2][2] and grid[0][2] != " " and grid[1][2] == " " and grid[0][2] == "o":
        target = [1,2]
        return True
    elif grid[1][2] == grid[2][2] and grid[1][2] != " " and grid[0][2] == " " and grid[1][2] == "o":
        target = [0,2]
        return True
    elif grid[0][0] == grid[1][1] and grid[1][1] != " " and grid[2][2] == " " and grid[0][0] == "o":
        target = [2,2]
        return True
    elif grid[0][0] == grid[2][2] and grid[0][0] != " " and grid[1][1] == " " and grid[0][0] == "o":
        target = [1,1]
        return True
    elif grid[1][1] == grid[2][2] and grid[1][1] != " " and grid[0][0] == " " and grid[1][1] == "o":
        target = [0,0]
        return True
    elif grid[2][0] == grid[1][1] and grid[1][1] != " " and grid[0][2] == " " and grid[2][0] == "o":
        target = [0,2]
        return True
    elif grid[2][0] == grid[0][2] and grid[2][0] != " " and grid[1][1] == " " and grid[2][0] == "o":
        target = [1,1]
        return True
    elif grid[1][1] == grid[0][2] and grid[1][1] != " " and grid[2][0] == " " and grid[1][1] == "o":
        target = [2,0]
        return True
    else:
        return False

def bar(grid):#defensive
    if grid[0][0] == grid[0][1] and grid[0][0] != " " and grid[0][2] == " " and grid[0][0] == "X":
        global target
        target = [0,2]
        return True
    elif grid[0][0] == grid[0][2] and grid[0][0] != " " and grid[0][1] == " " and grid[0][0] == "X":
        target = [0,1]
        return True
    elif grid[0][1] == grid[0][2] and grid[0][1] != " " and grid[0][0] == " " and grid[0][1] == "X":
        target = [0,0]
        return True
    elif grid[1][0] == grid[1][1] and grid[1][0] != " " and grid[1][2] == " " and grid[1][0] == "X":
        target = [1,2]
        return True
    elif grid[1][0] == grid[1][2] and grid[1][0] != " " and grid[1][1] == " " and grid[1][0] == "X":
        target = [1,1]
        return True
    elif grid[1][1] == grid[1][2] and grid[1][1] != " " and grid[1][0] == " " and grid[1][1] == "X":
        target = [1,0]
        return True
    elif grid[2][0] == grid[2][1] and grid[2][0] != " " and grid[2][2] == " " and grid[2][0] == "X":
        target = [2,2]
        return True
    elif grid[2][0] == grid[2][2] and grid[2][0] != " " and grid[2][1] == " " and grid[2][0] == "X":
        target = [2,1]
        return True
    elif grid[2][1] == grid[2][2] and grid[2][1] != " " and grid[2][0] == " " and grid[2][1] == "X":
        target = [2,0]
        return True
    elif grid[0][0] == grid[2][0] and grid[0][0] != " " and grid[1][0] == " " and grid[0][0] == "X":
        target = [1,0]
        return True
    elif grid[0][0] == grid[1][0] and grid[0][0] != " " and grid[2][0] == " " and grid[0][0] == "X":
        target = [2,0]
        return True
    elif grid[1][0] == grid[2][0] and grid[1][0] != " " and grid[0][0] == " " and grid[1][0] == "X":
        target = [0,0]
        return True
    elif grid[0][1] == grid[1][1] and grid[0][1] != " " and grid[2][1] == " " and grid[0][1] == "X":
        target = [2,1]
        return True
    elif grid[0][1] == grid[2][1] and grid[0][1] != " " and grid[1][1] == " " and grid[0][1] == "X":
        target = [1,1]
        return True
    elif grid[1][1] == grid[2][1] and grid[1][1] != " " and grid[0][1] == " " and grid[1][1] == "X":
        target = [0,1]
        return True
    elif grid[0][2] == grid[1][2] and grid[1][2] != " " and grid[2][2] == " " and grid[0][2] == "X":
        target = [2,2]
        return True
    elif grid[0][2] == grid[2][2] and grid[0][2] != " " and grid[1][2] == " " and grid[0][2] == "X":
        target = [1,2]
        return True
    elif grid[1][2] == grid[2][2] and grid[1][2] != " " and grid[0][2] == " " and grid[1][2] == "X":
        target = [0,2]
        return True
    elif grid[0][0] == grid[1][1] and grid[1][1] != " " and grid[2][2] == " " and grid[0][0] == "X":
        target = [2,2]
        return True
    elif grid[0][0] == grid[2][2] and grid[0][0] != " " and grid[1][1] == " " and grid[0][0] == "X":
        target = [1,1]
        return True
    elif grid[1][1] == grid[2][2] and grid[1][1] != " " and grid[0][0] == " " and grid[1][1] == "X":
        target = [0,0]
        return True
    elif grid[2][0] == grid[1][1] and grid[1][1] != " " and grid[0][2] == " " and grid[2][0] == "X":
        target = [0,2]
        return True
    elif grid[2][0] == grid[0][2] and grid[2][0] != " " and grid[1][1] == " " and grid[2][0] == "X":
        target = [1,1]
        return True
    elif grid[1][1] == grid[0][2] and grid[1][1] != " " and grid[2][0] == " " and grid[1][1] == "X":
        target = [2,0]
        return True
    else:
        return False

def corner(grid):#random corner
    global target
    target = random.choice([[0, 0], [2, 0], [0, 2], [2, 2]])
    while grid[target[0]][target[1]] != " ":
        target = random.choice([[0, 0], [2, 0], [0, 2], [2, 2]])
    return target

def adj(pos, distance, side):#adjacent positions
    global target
    if pos == [0, 0]:
        if distance == 1:
            if side == "c/":
                target = [0, 1]
                return target
            else:
                target = [1, 0]
                return target
        else:
            if side == "c/":
                target = [0, 2]
                return target
            else:
                target = [2, 0]
                return target
    elif pos == [0, 2]:
        if distance == 1:
            if side == "c/":
                target = [1, 2]
                return target
            else:
                target = [0, 1]
                return target
        else:
            if side == "c/":
                target = [2, 2]
                return target
            else:
                target = [0, 0]
                return target
    elif pos == [2, 0]:
        if distance == 1:
            if side == "c/":
                target = [1, 0]
                return target
            else:
                target = [2, 1]
                return target
        else:
            if side == "c/":
                target = [0, 0]
                return target
            else:
                target = [2, 2]
                return target
    else:
        if distance == 1:
            if side == "c/":
                target = [2, 1]
                return target
            else:
                target = [1, 2]
                return target
        else:
            if side == "c/":
                target = [2, 0]
                return target
            else:
                target = [0, 2]
                return target

def opp(pos):#opposite positions for corners
    for n in range(0,2):
        if pos[n] == 0:
            pos[n] = 2
        else:
            pos[n] = 0
    global target
    target = pos

#main
board = [[" ", " ", " "], 

         [" ", " ", " "], 

         [" ", " ", " "]]
p1 = random.choice([True, False])
count = 1
check = 0
while not wincheck(board) and count <= 9:
    if p1:
        displaygrid(board)
        print("Your turn:")
        row, col = int(input("Row: ")), int(input("Column: "))
        while row < 1 or row > 3 or col < 1 or col > 3:
            print("Not valid. Re-enter:")
            row, col = int(input("Row: ")), int(input("Column: "))

        row -= 1
        col -= 1
        while board[row][col] != " ":
            print("Not valid. Re-enter:")
            row, col = int(input("Row: ")), int(input("Column: "))
        
        board[row][col] = "X"
    else:
        if off(board):
            row, col = target[0], target[1]
        elif bar(board):
            row, col = target[0], target[1]
        elif count == 1:
            start = corner(board)
            row, col = start[0], start[1]
        elif count == 2:
            if board[1][1] == " ":
                row = col = 1
            else:
                corner(board)
                row, col = target[0], target[1]
        elif count == 3:
            if board[1][1] == "X":
                opp(start)
                row, col = target[0], target[1]
            else:
                adj(start, 2, "a/c")
                if board[target[0]][target[1]] == "X":
                    adj(start, 2, "c/")
                    row, col = target[0], target[1]
                adj(start, 1, "a/c")
                if board[target[0]][target[1]] == "X":
                    adj(start, 2, "c/")
                    row, col = target[0], target[1]
                if check == 0:
                    adj(start, 2, "a/c")
                    row, col = target[0], target[1]
        elif count == 4:
            if board[1][1] == "o":
                target = random.choice([[0, 1], [1, 0], [1, 2], [2, 1]])
                while board[target[0]][target[1]] != " ":
                    target = random.choice([[0, 1], [1, 0], [1, 2], [2, 1]])
                row, col = target[0], target[1]
            else:
                corner(board)
                row, col = target[0], target[1]
        elif count == 5:
            adj(start, 2, "a/c")
            if board[target[0]][target[1]] == "X":
                opp(start)
                row, col = target[0], target[1]
                check += 1
            adj(start, 1, "a/c")
            if board[target[0]][target[1]] == "X":
                opp(start)
                row, col = target[0], target[1]
                check += 1
            if check == 1:
                adj(start, 2, "a/c")
                row, col = target[0], target[1]
        else:
            target = random.choice([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
            while board[target[0]][target[1]] != " ":
                print("randomizing")
                target = random.choice([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
            row, col = target[0], target[1]
        board[row][col] = "o"
    p1 = not p1
    count += 1

displaygrid(board)
if winner == "X":
    print("\nYou win!\nGame Over.")
elif winner == "o":
    print("\nComputer wins!\nGame Over.")
else:
    print("\nDraw.\nGame Over.")
