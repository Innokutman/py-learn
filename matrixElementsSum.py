# https://app.codesignal.com/arcade/intro/level-2/xskq4ZxLyqQMCLshr
def matrixElementsSum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i-1][j] == 0) and (i != 0):
                matrix[i][j] = 0
            sum += matrix[i][j]
    return sum
print(matrixElementsSum([
[0,1,1,2], 
[0,5,0,0], 
[2,0,3,3]]))        
