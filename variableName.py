# https://app.codesignal.com/arcade/intro/level-6/6Wv4WsrsMJ8Y2Fwno
def variableName(name):
    str_name = [i for i in str(name)]
    declined = [" ", ">", "<", ":", "-", "|", ".", ",", "!", "[", "]", "'", "/", "@", "#", "&", "%", "?", "*"]
    if str_name[0] in str([0,1,2,3,4,5,6,7,8,9]):
        return False
    for j in range(len(str_name)):
        if str_name[j] in decline:
            return False
    return True

    # def variableName(name):
    # return name.isidentifier()  - what a fuckkkkkkk???
    # def variableName(name):

    # if re.match('[a-z_][0-9_a-z]*$', name,re.IGNORECASE):
    #     return True
    # return False