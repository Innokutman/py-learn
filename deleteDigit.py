# https://app.codesignal.com/arcade/intro/level-11/vpfeqDwGZSzYNm2uX
def deleteDigit(n):
    num = str(n)
    biggest = 0
    for digit in range(len(num)):
        lower = num[:digit] + num[digit + 1:]
        if int(lower) > int(biggest):
            biggest = lower
    return int(biggest)

# def deleteDigit(n):
#     ret = 0
#     n = str(n)
#     for i in range(len(n)):
#         ret = max(ret, int(n[:i] + n[i + 1:]))
#     return ret