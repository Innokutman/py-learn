# https://app.codesignal.com/arcade/intro/level-12/sqZ9qDTFHXBNrQeLC
def fileNaming(names):
    falseNames = []
    for name in names:
        if name in falseNames:
            k = 1
            while "{}({})".format(name, k) in falseNames:
                k += 1
            name = "{}({})".format(name, k)
        falseNames.append(name)
    return falseNames
