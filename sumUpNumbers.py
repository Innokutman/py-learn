# https://app.codesignal.com/arcade/intro/level-12/YqZwMJguZBY7Hz84T
def sumUpNumbers(inputString):
    result = 0
    current_number = []
    for char in inputString:
        if char.isdigit():
            current_number.append(char)
        else:
            if len(current_number) > 0:
                num = int("".join(current_number))
                result += num
                current_number = []
    if len(current_number) > 0:
        num = int("".join(current_number))
        result += num
    return result
# def sumUpNumbers(inputString):
#     l = re.findall(r"\d+",inputString)
#     return sum([int(i) for i in l])

# def sumUpNumbers(inputString):
#     sum1 = 0
#     temp1 = re.findall(r'\d+', inputString)
#     if len(temp1)>0:
#         for i in temp1:
#             temp = 0
#             temp = int(i,10)
#             sum1 = sum1 + temp
#     return sum1