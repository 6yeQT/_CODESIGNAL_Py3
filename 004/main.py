def sudoku2(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            val = grid[i][j]
            if val is not '.':
                row, col = i, j
                for x in range(col+1, 9):
                    if val == grid[row][x]:
                        return False
                    grid3xMax = 9 if x > 6 else x + 3
                    grid3xMin = 0 if x < 3 else x - 3
                    for grid3x in range(grid3xMin, grid3xMax):
                        if val == grid[row][grid3x]:
                            return False

                for y in range(row+1, 9):
                    if val == grid[y][col]:
                        return False
                    grid3yMax = 9 if y > 6 else y+3
                    grid3yMin = 0 if y < 3 else y-3

                    for grid3y in range(grid3yMin, grid3yMax):
                        if val == grid[grid3y][col]:
                            return False
    return True





grid =  [[".",".","5",".",".",".",".",".","."],
         [".",".",".","8",".",".",".","3","."],
         [".","5",".",".","2",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","9"],
         [".",".",".",".",".",".","4",".","."],
         [".",".",".",".",".",".",".",".","7"],
         [".","1",".",".",".",".",".",".","."],
         ["2","4",".",".",".",".","9",".","."]]
# grid2 = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
#         ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
#         ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
#         ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
#         ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
#         ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
#         ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
#         ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
#         ['.', '2', '.', '.', '3', '.', '.', '.', '.']]

print('sudoku 1: ', sudoku2(grid))
# print('sudoku 2: ', sudoku2(grid2))
