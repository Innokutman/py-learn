# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(inputArray):
    # max = inputArray[0] + inputArray[1]
    # for i in range (len(inputArray) - 1):
    #     for j in range (i + 1, len(inputArray)):
    #         s = inputArray[i] + inputArray[j]
    #         print(str(inputArray[i]) + " + " + str(inputArray[j]) + " = " + str(s))
    #         if s > max:
    #             max = s
    # return max
    a = sorted(inputArray, reverse = True)
    return a[0] + a[1]

print(adjacentElementsProduct([3, 11, -2, 1, 5]))