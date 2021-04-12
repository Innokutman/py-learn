# https://app.codesignal.com/arcade/intro/level-12/tQgasP8b62JBeirMS
def sudoku(grid):
    nums = [0]*9
    for i in range(0, 9):
        nums = [0]*9
        for j in range(0, 9):
            nums[grid[i][j]-1] += 1
            if nums[grid[i][j]-1] >= 2:
                return False
    for i in range(0, 9):
        nums = [0]*9
        for j in range(0, 9):
            nums[grid[j][i]-1] += 1
            if nums[grid[j][i]-1] >= 2:
                return False            
    for x in range(0, 3):
        for y in range(0, 3):
            nums = [0]*9
            for i in range(0, 3):
                for j in range(0 ,3):
                    nums[grid[x*3+i][3*y+j]-1] += 1
                    if nums[grid[x*3+i][3*y+j]-1] >= 2:
                        return False
    return True