# https://app.codesignal.com/arcade/intro/level-5/g6dc9KJyxmFjB98dL
def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    my_max = max(yourLeft, yourRight)
    friends_max = max(friendsLeft, friendsRight)
    sum1 = yourLeft + yourRight
    sum2 = friendsLeft + friendsRight
    if sum1 == sum2 and my_max == friends_max:
        return True
    return False