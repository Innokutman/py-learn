# https://app.codesignal.com/arcade/intro/level-12/NJJhENpgheFRQbPRA
def digitsProduct(product):
    for i in range(1, 10000):
        number = str(i)
        total = 1
        
        for char in number:
            total *= int(char)
        if total == product:
            return i
    return -1

