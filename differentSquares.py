# https://app.codesignal.com/arcade/intro/level-12/fQpfgxiY6aGiGHLtv
def differentSquares(matrix):
    squares=[]
    count = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            square=[matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
            if square not in squares:
                squares.append(square)
                count+=1
    return count
# def differentSquares(matrix):
#     squares = set()
#     for row in range(len(matrix) - 1):
#         for cell in range(len(matrix[row]) - 1):
#             square = ((matrix[row][cell], matrix[row][cell + 1]),
#                       (matrix[row + 1][cell], matrix[row + 1][cell + 1]))
#             squares.add(square)
#     return len(squares)