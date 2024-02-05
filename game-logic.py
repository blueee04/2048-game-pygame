import random

def move(dir,board):
    if(dir == "w"):
        return move_up(board)
    if(dir == "s"):
        return move_down(board)
    if(dir == "a"):
        return move_left(board)
    if(dir == "d"):
        return move_right(board)
    
def Check_Status(board,max = 4096):
    for i in range(4):
        for j in range(4):
            if(board[i][j] == max):
                return "win"
    for i in range(4):
        for j in range(4):
            if(board[i][j] == 0):
                return "KEEP PLAYING"
    for i in range(3):
        for j in range(3):
            if(board[i][j] == board[i+1][j] or board[i][j] == board[i][j+1]):
                return "KEEP PLAYING"
    for i in range(3):
        if(board[i][3] == board[i+1][3]):
            return "KEEP PLAYING"
    for j in range(3):
        if(board[3][j] == board[3][j+1]):
            return "KEEP PLAYING"
    return "YOU LOST"

def fill2_4(board):
    a = random.randint(0,3)
    b = random.randint(0,3)
    while(board[a][b] != 0):
        a = random.randint(0,3)
        b = random.randint(0,3)
    return board
    if sum([i for row in board for i in row]) in (0,2):
        board[a][b] = 2
    else:
        board[a][b] = random.choice([2,4])

def move_left(board):
    for i in range(4):
        board[i] = slide(board[i])
        board[i] = merge(board[i])
        board[i] = slide(board[i])
    return board

def slide(row):
    return [i for i in row if i != 0] + [0]*row.count(0)

def merge(row):
    for i in range(3):
        if row[i] == row[i+1]:
            row[i] *= 2
            row[i+1] = 0
    return row
