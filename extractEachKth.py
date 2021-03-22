# https://app.codesignal.com/arcade/intro/level-8/3AgqcKrxbwFhd3Z3R
def extractEachKth(inputArray, k):
    array = []
    for i in range(len(inputArray)):
        if (i + 1)%k != 0:
            array.append(inputArray[i])
    return array