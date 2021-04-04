# https://app.codesignal.com/arcade/intro/level-11/o2uq6eTuvk7atGadR
def lineEncoding(s):
    temp = ""
    prev = ""
    result = ""
    for i in s:
        if temp == "" or prev == i:
            temp = temp + i
        else:
            temp = temp + "-" + i
        prev = i
    list = temp.split("-")
    for j in list:
        if len(j) == 1:
            result = result + j
        else:
            count = str(len(j))
            result = result + count + j[0]
    return result