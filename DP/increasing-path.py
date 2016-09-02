# -*- coding: latin-1 -*-

"""
increasing path in a 2d grid
[row][col]
"""

def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]: 
        return 0
    row = len(matrix)
    col = len(matrix[0])
    dp = [[0] * col for i in range(row)]
    return max(fill(x, y, matrix, dp) for x in range(row) for y in range(col))

def fill(i, j, matrix, dp):
    row = len(matrix)
    col = len(matrix[0])

    if dp[i][j] == 0:
        val = matrix[i][j]
        paths = []
        #i-1,j
        #i+1,j
        #i, j+1
        #i, j-1
        if i and val > matrix[i - 1][j]:
            paths.append(fill(i - 1, j, matrix, dp))
        else: 
            paths.append(0)

        if i < row - 1 and val > matrix[i + 1][j]:
            paths.append(fill(i + 1, j, matrix, dp))
        else:
            paths.append(0)

        if j and val > matrix[i][j - 1]:
            paths.append(fill(i, j - 1, matrix, dp)) 
        else:
            paths.append(0)

        if j < col - 1 and val > matrix[i][j + 1]:
            paths.append(fill(i, j + 1, matrix, dp))
        else:
            paths.append(0)

        dp[i][j] = 1 + max(paths)
        
    return dp[i][j]


def main():
    grid = [
              [1 ,2 ,3 ,4 ,5],
              [16,17,24,23,6],
              [15,18,25,22,7],
              [14,19,20,21,8],
              [13,12,11,10,9]
            ]
    grid2 = [
                [2, 3, 4, 5],
                [4, 5, 10, 11], 
                [20, 6, 9, 12], 
                [6, 7, 8, 40]
            ]
    grid3 = [[1]]
    print longestIncreasingPath(grid)
    print longestIncreasingPath(grid2)
    print longestIncreasingPath(grid3)


if __name__ == '__main__':
    main()