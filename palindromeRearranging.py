# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
def palindromeRearranging(inputString):
    count = 0
    group = set(inputString)
    for i in group:
        group_count = inputString.count(i)
        if group_count % 2 != 0:
            count += 1
    if count <= 1:
        return True
    return False

print(palindromeRearranging("aabbbaa"))