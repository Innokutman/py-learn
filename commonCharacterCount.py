# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
def commonCharacterCount(s1, s2):
    s1 = [x for x in s1]
    s2 = [x for x in s2]
    sum = 0
    while len(s1) > 0:
        # print(s1, s2)
        x = 0
        while x < len(s2):
            print(s2, x)
            if s1[0] == s2[x]:
                sum += 1
                s2.pop(x)
                break
            x = x + 1
        s1.pop(0)

    # for x in s1: 
    #     for y in s2:
    #         if x == y:
    #             sum  += 1

    return sum
    
print(commonCharacterCount("aabcc", "vdmfz"))