# https://app.codesignal.com/arcade/intro/level-10/8RiRRM3yvbuAd3MNg
def electionsWinners(votes, k):
    Trump = max(votes)
    count = 0
    if k ==0 and votes.count(Trump) == 1:
        return 1
    for i in votes:
        if k + i > Trump:
            count += 1
    return count