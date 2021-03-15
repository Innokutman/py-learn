# https://app.codesignal.com/arcade/intro/level-7/ZFnQkq9RmMiyE6qtq
import statistics
def absoluteValuesSumMinimization(a):
    sumMinmimization = []
    length = len(a)
    median = 0
    result = a[0]
    median = statistics.median(a)
    for j in range(length):
        if abs(a[i] - median) < abs(result - median):
            result = a[i]
    return result




