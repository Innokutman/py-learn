# https://app.codesignal.com/arcade/intro/level-10/ppZ9zSufpjyzAsSEx/solutions
def buildPalindrome(st):
    for i in range(len(st)):
        check = st[i:len(st)]
        if check[::-1] == check: 
            add = st[0:i]
            return st + add[::-1]
    return st