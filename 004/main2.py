def sudoku2(grid):
    for i in range(0, 9):
        for j in range(0, 9):
            val = grid[i][j]
            #print('val ', val)
            if val is not '.':
                row, col = i, j
                for x in range(col+1, 9):
                    if val == grid[row][x]:
                        return False
                    grid3xMax = 9 if x > 6 else x+3

                    for grid3x in range(x, grid3xMax):
                        if val == grid[row][grid3x]:
                            return False
                for y in range(row+1, 9):
                    grid3yMax = 9 if y > 6 else y+3

                    for grid3y in range(y, grid3yMax):
                        if val == grid[grid3y][col]:
                            return False
                    if val == grid[y][col]:
                        return False

    return True