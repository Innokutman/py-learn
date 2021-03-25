# https://app.codesignal.com/arcade/intro/level-9/r9azLYp2BDZPyzaG2
def knapsackLight(value1, weight1, value2, weight2, maxW):
    return max(int(weight1 <= maxW) * value1, int(weight2 <= maxW) * value2, int(weight1 + weight2 <= maxW) * (value1 + value2))
    # def knapsackLight(v1, w1, v2, w2, maxW):
    # if not w1 + w2 > maxW:
    #     return v1 + v2
    # elif w2 <= maxW and v2 > v1:
    #     return v2
    # elif w1 <= maxW:   
    #     return v1
    # else:
    #     return 0