# https://app.codesignal.com/arcade/intro/level-2/xzKiBHjhoinnpdh6m
def adjacentElementsProduct(inputArray):
    return max([inputArray[i] + inputArray[i+1] for i in range(len(inputArray)-1)])
print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))