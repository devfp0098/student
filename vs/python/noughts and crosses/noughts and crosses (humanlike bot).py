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

#main
board = [[" ", " ", " "], 

         [" ", " ", " "], 

         [" ", " ", " "]]
p1 = random.choice([True, False])
game = not p1
count = 1
while not wincheck(board) and count <= 9:
    if p1:
        displaygrid(board)
        print("Your turn:")
        row, col = int(input("Row: ")), int(input("Column: "))
        while row < 1 or row > 3 or col < 1 or col > 3:
            displaygrid(board)
            print("Not valid. Re-enter:")
            row, col = int(input("Row: ")), int(input("Column: "))

        row -= 1
        col -= 1
        while board[row][col] != " ":
            displaygrid(board)
            print("Not valid. Re-enter:")
            row, col = int(input("Row: ")), int(input("Column: "))
        
        board[row][col] = "X"

    else:
        if off(board):
            row, col = target[0], target[1]
        elif bar(board):
            row, col = target[0], target[1]
        else:
            target = random.choice([[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2]])
            while board[target[0]][target[1]] != " ":
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