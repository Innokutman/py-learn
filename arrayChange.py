# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
def arrayChange(inputArray):
    a = inputArray[0]
    count = 0
    for i in inputArray[1:]:
        if i <= a:
            count += a - i + 1
            a = a + 1
        else:
            a = i
    return count