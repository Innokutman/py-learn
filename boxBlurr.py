# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
def boxBlur(image):

    row = []
    for i in range(len(image)-2):
        row.append([])
        for j in range(len(image[0])-2):
            row[i].append(sum(image[i][j:j+3] + image[i+1][j:j+3] + image[i+2][j:j+3])/9//1)
    return row