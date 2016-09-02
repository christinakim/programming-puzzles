"""
robot in a grid

imagine a robot sitting on the upper left corner of a grid with r rows and c colums
the robot can only move in two directions right and down but certain cells are off limits aka robot can't step on them

algorithm to lead robot to top left to bottom right

subproblem is do we go right or down

let's start from the bottom corner 
moving left row, col-1
moving up row + 1, col
"""
from timeit import timeit

def robot_path(r, c, grid, path = [], memo = {}):
    path_found = False
    origin = r == 0 and c == 0

    if (r,c) in memo:
        return memo[(r,c)]
    else:
        if r < 0 or c < 0:
            return path_found
        if origin:
            path.append([r,c])
            path_found = True
            memo[(r,c)] = path_found
            return path_found 
        else:
            if grid[r][c - 1] and c > 0:
                path.append([r,c - 1])
                path_found = True
                memo[(r,c)] = path_found
                robot_path(r - 1, c, grid, path, memo)

            if grid[r - 1][c] and r > 0:
                #try up
                path.append([r - 1, c])
                path_found = True
                memo[(r,c)] = path_found
                robot_path(r, c - 1, grid, path, memo)



        memo[(r,c)] = path_found

        return path_found

grid = [[True, True, True, True],[True, True, True, True],[True, True, True, True], [True, False, False, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True], [True, False, False, True],[True, True, True, True]]
r = 4
c = 3


r = 4
c = 3


print timeit('robot_path(8, 3, [[True, True, True, True],[True, True, True, True],[True, True, True, True], [True, False, False, True],[True, True, True, True],[True, True, True, True],[True, True, True, True],[True, True, True, True], [True, False, False, True],[True, True, True, True]])', setup = 'from __main__ import robot_path')