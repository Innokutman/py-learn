# https://app.codesignal.com/arcade/intro/level-6/mCkmbxdMsMTjBc3Bm
def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for i in range(len(inputArray)):
        if inputArray[i] == elemToReplace:
            inputArray[i] = substitutionElem
    return inputArray