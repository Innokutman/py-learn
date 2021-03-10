# https://app.codesignal.com/arcade/intro/level-3/9DgaPsE2a7M6M2Hu6
def reverseInParentheses(inputString):
    for i in range(len(inputString)):
        if inputString[i] == "(":
            start = i
        if inputString[i] == ")":
            end = i
            return reverseInParentheses(inputString[:start] + inputString[start+1:end][::-1] + inputString[end+1:])
    return inputString