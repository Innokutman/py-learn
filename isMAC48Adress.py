# https://app.codesignal.com/arcade/intro/level-10/HJ2thsvjL25iCvvdm
import re
def isMAC48Address(inputString):
    if re.match("[0-9a-f]{2}([-:])[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", inputString.lower()):
            return True
    else:
            return False