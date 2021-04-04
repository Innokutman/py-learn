# https://app.codesignal.com/arcade/intro/level-11/pwRLrkrNpnsbgMndb
def chessKnight(cell):
    moves = 0
    if ord(cell[0]) >= ord("b") and ord(cell[1]) <= ord("6"):
        moves += 1
    if ord(cell[0]) >= ord("c") and ord(cell[1]) <= ord("7"):
        moves += 1
    if ord(cell[0]) >= ord("c") and ord(cell[1]) >= ord("2"):
        moves += 1
    if ord(cell[0]) >= ord("b") and ord(cell[1]) >= ord("3"):
        moves += 1
    if ord(cell[0]) <= ord("g") and ord(cell[1]) >= ord("3"):
        moves += 1
    if ord(cell[0]) <= ord("f") and ord(cell[1]) >= ord("2"):
        moves += 1
    if ord(cell[0]) <= ord("f") and ord(cell[1]) <= ord("7"):
        moves += 1
    if ord(cell[0]) <= ord("g") and ord(cell[1]) <= ord("6"):
        moves += 1

    return moves

    # def chessKnight(cell):
    # pos = ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2))
    # return sum(map(lambda x: 1 <= int(cell[0], 18) - 9 + x[0] <= 8 and 1 <= int(cell[1]) + x[1] <= 8, pos)) need poyasnitelnaya brigada