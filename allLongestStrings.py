# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL/solutions
def allLongestStrings(inputArray):
    a = sorted(inputArray, key = len, reverse = True)
    print(a)
    b = []
    for i in range(len(a)):
        if (i == 0) or (len(a[i]) == len(a[i-1])):
            b.append(a[i])
        else:
            break
        print(b)
    return b

allLongestStrings(["aba", 
 "aa", 
 "ad", 
 "vcd", 
 "aba"])