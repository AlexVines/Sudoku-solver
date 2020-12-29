import numpy as np
import sudoku_gui
import time

grid = [[5, 3, 0,   0, 7, 0,    0, 0, 0],
        [6, 0, 0,   1, 9, 5,    0, 0, 0],
        [0, 9, 8,   0, 0, 0,    0, 6, 0],

        [8, 0, 0,   0, 6, 0,    0, 0, 3],
        [4, 0, 0,   8, 0, 3,    0, 0, 1],
        [7, 0, 0,   0, 2, 0,    0, 0, 6],

        [0, 6, 0,   0, 0, 0,    2, 8, 0],
        [0, 0, 0,   4, 1, 9,    0, 0, 5],
        [0, 0, 0,   0, 8, 0,    0, 7, 9],
]

# grid = [[0, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#
#         [0, 0, 0,   0, 0, 0,    0, 8, 0],
#         [0, 0, 0,   0, 0, 0,    0, 0, 0],
#         [0, 0, 0,   0, 8, 0,    0, 0, 0],
# ]

def possible(y, x, n):
    global grid
    for i in range(0,9):
        if grid[y][i] == n:
            return False
    for i in range(0, 9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[y0+i][x0+j] == n:
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i !=0:
            print('- - - - - - - - - - - ')

        for j in range (len(bo[0])):
            if j % 3 == 0 and j != 0:
                print ('│', end="")
            if j == 8:
                print(grid[i][j])
            else:
                print(str(grid[i][j]) + ' ', end="")


def solver(grid):
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if possible(y, x, n):
                        grid[y][x] = n
                        solver(grid)
                        grid[y][x] = 0

                return
    print_board(grid)

solver(grid)


