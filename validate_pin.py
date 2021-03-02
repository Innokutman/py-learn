#https://www.codewars.com/kata/55f8a9c06c018a0d6e000132/train/python
def validate_pin(pin):
    l = len(pin)
    if (l == 4) or (l == 6):
        for x in pin:
            o = ord(x)
            if (o < 48) or (o > 57):
                return False
        return True
    return False
