# https://app.codesignal.com/arcade/intro/level-9/hoLtYWbjdrD2PF6yo
def digitDegree(n):
    count = 0
    while 10 <= n:
        digit = str(n)
        n = sum(int(i) for i in digit)
        count += 1
    return count
print(digitDegree(777773))
# # def _sumOfDigits(n, m):
# #     digits = str(n)
# #     if len(digits) == 0:
# #         return m
# #     else:
# #         m += int(digits[0])
# #         return _sumOfDigits(digits[1:], m)
# # def sumOfDigits(n):
# #     _sumOfDigits(n, 0)
# # def digitDegree(n):
# #     digits = str(n)
# #     count = 0
# #     result = n
# #     if len(digits) == 1:
# #         return 0
# #     else:
# #         while len(str(result)) != 1:
# #             result = sumOfDigits(result)
# #             count += 1
# #         return count
