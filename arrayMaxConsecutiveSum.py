# https://app.codesignal.com/arcade/intro/level-8/Rqvw3daffNE7sT7d5
def arrayMaxConsecutiveSum(inputArray, k):
    actualSum = maxSum = sum(inputArray[:k])
    for i in range(len(inputArray) - k):
        actualSum = actualSum + inputArray[i + k] - inputArray[i]
        maxSum = max(actualSum, maxSum)
    return maxSum
print(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2))

# def arrayMaxConsecutiveSum(a, k):
#     c = m = sum(a[:k])
    
#     for i in range(len(a) - k):
#         c = c + a[i + k] - a[i]
#         m = max(c, m)
        
#     return m
