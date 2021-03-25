# https://app.codesignal.com/arcade/intro/level-9/xHvruDnQCx7mYom3T  
def growingPlant(upSpeed, downSpeed, desiredHeight):
    day = 0
    height = 0
    while height <= desiredHeight:
        height = height + upSpeed
        day += 1
        if height < desiredHeight:
            height = height - downSpeed
        else:
            return day
# def growingPlant(upSpeed, downSpeed, desiredHeight):
#     if desiredHeight <= upSpeed:
#         return 1
#     return math.ceil((desiredHeight - upSpeed) / (upSpeed - downSpeed) + 1)