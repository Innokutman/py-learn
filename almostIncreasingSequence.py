# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG
def almostIncreasingSequence(sequence):
    c0,c1=1,1
    n=len(sequence)
    l1=[]
    l2=[]
    for i in sequence:
        l1.append(i)
        l2.append(i)
    for i in range(1,n):
        if sequence[i-1]>=sequence[i]:
            del l1[i]
            del l2[i-1]
            break
        print(l1)
        print(l2)
    for i in range(1,n-1):
        if l1[i-1]>=l1[i]:
            c0=0
            break
        print(l1)
        print(l2)
    for i in range(1,n-1):
        if l2[i-1]>=l2[i]:
            c1=0
            break
        print(l1)
        print(l2)
    return bool(c0 or c1)
print(almostIncreasingSequence([1, 3, 2, 1]))

# https://stackoverflow.com/questions/43017251/solve-almostincreasingsequence-codefights - ????