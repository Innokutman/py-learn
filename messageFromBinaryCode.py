# https://app.codesignal.com/arcade/intro/level-12/sCpwzJCyBy2tDSxKW/solutions
def messageFromBinaryCode(code):
    ret = ""
    for i in range(0, len(code), 8):
        num = int(code[i:i + 8], 2)
        ret += chr(num)
    return ret