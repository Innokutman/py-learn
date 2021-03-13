#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def evenDigitsOnly(n):

    inputArray = str(n)
    isEvenDigitsOnly = True
    for i in range(len(inputArray)):
        if int(inputArray[i]) % 2 != 0:
            isEvenDigitsOnly = False
    return isEvenDigitsOnly
