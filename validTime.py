# https://app.codesignal.com/arcade/intro/level-12/ywMyCTspqGXPWRZx5
def validTime(time):
    time_split = time.split(":")
    if 00 <= int(time_split[0]) <= 23 and 00 <= int(time_split[1]) <= 59:
        return True
    return False

# import time as t
# def validTime(time):
#     try: t.strptime(time, "%H:%M")
#     except: return False
#     return True