def sortByHeight(a):
    sort = sorted([i for i in a if i!=-1])
    counter = 0
    for i in range(len(a)):
        if a[i] == -1:
            pass
        else:
            a[i]=sort[counter]
            counter+=1
    return a