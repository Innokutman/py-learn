# https://app.codesignal.com/arcade/intro/level-5/EEJxjQ7oo7C5wAGjE
def arrayMaximalAdjacentDifference(inputArray):
    maximum = 0
    for i in range (0, len(inputArray) - 1):
        production = abs(inputArray[i+1] - inputArray[i])
        if production > maximum:
            maximum = production
    return maximum
print(arrayMaximalAdjacentDifference([2, 4, 1, 0]))

#    return max([abs(i - j) for i, j in zip(inputArray, inputArray[1:])])