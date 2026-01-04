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
#main
board = [[" ", " ", " "], 

         [" ", " ", " "], 

         [" ", " ", " "]]
p1 = random.choice([True, False])
count = 1
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
        row, col = random.randint(0, 2), random.randint(0, 2)
        while board[row][col] != " ":
            row, col = random.randint(0, 2), random.randint(0, 2)

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