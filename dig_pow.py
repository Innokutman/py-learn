#https://www.codewars.com/kata/5552101f47fc5178b1000050/train/python
def dig_pow(n, p):
    l = []
    m = n
    while n > 0:
        l.append(n % 10)
        n = n // 10
    # print(l[::-1])
    l = l[::-1]
    s = 0
    for x in l: 
        s += x**p 
        p+=1
    k = s // m
    if k != 0:
        return k
    else:
        return -1
    
dig_pow(89, 1)
print(dig_pow(89, 1))