# https://app.codesignal.com/arcade/intro/level-10/PHSQhLEw3K2CmhhXE/drafts?solutionId=uto2vKvuhy6HjYreN
def isBeautifulString(inputString):
    for i in range(ord('a'), ord('z')):
        if inputString.count(chr(i)) < inputString.count(chr(i + 1)):
            return False
    return True