def findEmailDomain(address):
    split = address.split("@")
    c = [ i for i in split ]
    if len(split) == 2:
        return c[1]     
    if len(split) == 3:
        return c[2]
# def findEmailDomain(address):
#     a = address.split('@')
#     return a[-1] 
findEmailDomain("prettyandsimple@example.com")