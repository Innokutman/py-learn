# https://app.codesignal.com/arcade/intro/level-4/ZCD7NQnED724bJtjN
def addBorder(picture):
    a = []
    border = ""
    pic_len = len(picture)
    for i in range(0, len(picture[0])+2):
        border += "*"
    a.append(border)
    for i in range(0, pic_len):
        a.append("*" + picture[i] + "*")
    a.append(border)
    return a