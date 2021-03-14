# https://app.codesignal.com/arcade/intro/level-6/PWLT8GBrv9xXy4Dui
def alphabeticShift(i):
    i=list(i)
    for x in range(len(i)):
        if i[x] == 'z':
            i[x] = 'a'
            continue
        i[x] = chr(ord(i[x])+1)
    return "".join(i)

    # from string import ascii_lowercase as a
# def alphabeticShift(s):
    # return "".join([a[a.find(i)-25] for i in s])