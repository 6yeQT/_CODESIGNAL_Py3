def sudoku2(grid):
    temp = []
    for i in range(0, 9):
        for j in range(0, 9):
            val = grid[i][j]
            if val is not '.':
                temp.append((val, i//3, j//3))
                row, col = i, j
                for x in range(col+1, 9):
                    if val == grid[row][x]:
                        return False
                for y in range(row+1, 9):
                    if val == grid[y][col]:
                        return False
    print(temp)
    for i in range(len(temp)):
        for j in range(len(temp)):
            lala = temp[i]
            lala2= temp[j]
            if temp[i][0] == temp[j][0] and i != j:
                print('temp i ', temp[i])
                print('temp j ', temp[j])
                _, x1, y1 = temp[i]
                _, x2, y2 = temp[j]
                if (x1 == x2 and y1 == y2):
                    return False
    return True



grid = [ [".",".",".",".",".",".","5",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".",".",".",".",".",".","."],
         ["9","3",".",".","2",".","4",".","."],
         [".",".","7",".",".",".","3",".","."],
         [".",".",".",".",".",".",".",".","."],
         [".",".",".","3","4",".",".",".","."],
         [".",".",".",".",".","3",".",".","."],
         [".",".",".",".",".","5","2",".","."]]

print('sudoku 1: ', sudoku2(grid), 'exp: False')
