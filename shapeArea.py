# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ
def shapeArea(n):
    area = 0
    if (n == 1):
        area = 1
        return area
#     else: 
#         area = shapeArea(n - 1) + (n*2) + ((n-2)*2)
#         return area
# print(shapeArea(3))
    else: 
        # area = shapeArea(n - 1) + 4 * (n - 1)
        # return area     
        area = (2 + (n-2)*2) * (n-1) + 2*n - 1
        return area
print(shapeArea(8000))