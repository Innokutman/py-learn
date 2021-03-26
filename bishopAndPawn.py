# https://app.codesignal.com/arcade/intro/level-9/6M57rMTFB9MeDeSWo
def bishopAndPawn(bishop, pawn):
    if ord(bishop[0]) == ord(pawn[0]):
        return False
    else:
        pawnPosition = ord(pawn[0]) + int(pawn[1])
        bishopPosition = ord(bishop[0]) + int(bishop[1])
        return (bishopPosition + pawnPosition)%2 == 0
