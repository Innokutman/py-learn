def shapeArea(n):
    area = 0
    if (n == 1):
        area = 1
        return area
    else: 
        area = (n - 1) + (n*2) + ((n-2)*2)
        return area
print(shapeArea(10))