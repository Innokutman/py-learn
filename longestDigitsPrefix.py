# https://app.codesignal.com/arcade/intro/level-9/AACpNbZANCkhHWNs3
def longestDigitsPrefix(inputString):
    for i in range(len(inputString)):
        if not inputString[i].isdigit():
            return(inputString[0:i])
    return inputString

    # def longestDigitsPrefix(inputString):
    # return re.findall('^\d*',inputString)[0]

# check biggest sum on order to find line of numbers in any place of a list 