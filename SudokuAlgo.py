
from math import sqrt
import time

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 0, 3, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

#Function to solve sudoku with BackTracking algorithm
def solveSudoku(bo, self = None):
    # print(bo)

    nextEmpty = find_empty(bo)
    if not nextEmpty:
        return True
    else:
        row, col = nextEmpty
    for i in range(9):
        if isBoardValid(bo, row, col, i + 1):
            if (self):
                print("yes defined self inside sudoku")
                self.cubes[row][col].set(i + 1)
                # time.sleep(0.05)
            bo[row][col] = i + 1
            if solveSudoku(bo, self):
                return True
            bo[row][col] = 0
    return False

#function to print sudoku in nice way
def print_board(bo):
    size = len(bo)
    # print(bo)

    for i in range(size):
        print('')
        # print(bo[i])
        if i % sqrt(size) == 0 and i != 0:
            print('---------------------')
        for j in range(size):
            if j % sqrt(size) == 0 and j != 0:
                print("| ", end='')
            print(bo[i][j], end=' ')
            
    print('\n---------------------')


#Find first empty
def find_empty(bo):
    for i in range(0, len(bo)):
        for j in range(0, len(bo[i])):
            if (bo[i][j] == 0):
                return (i, j)
    return None


def isBoardValid(bo, row, col, num):
    #check for row
    for i in range(len(bo)):
        if (i != col and bo[row][i] == num):
            return False
    #check for column
    for i in range(len(bo)):
        if (i != row and bo[i][col] == num):
            return False
    #check for Box
    rowRep = row // 3 * 3     #Row representative is the row having row number = 0 or 3 or 6 etc
    colRep = col // 3 * 3
    for i in range(rowRep, rowRep + 3):
        for j in range(colRep, colRep + 3):
            
            if (i == row and j == col):
                continue
            if (bo[i][j] == num):
                return False
    return True

print_board(board)
solveSudoku(board)
print_board(board)