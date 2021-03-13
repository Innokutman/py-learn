# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
def avoidObstacles(inputArray): 

    inputArray = sorted(inputArray) 
    jump_distance = 1
    obstacle_suc = True
    while(obstacle_suc):   
        obstacle_suc = False
        jump_distance += 1
        for i in range(0, len(inputArray)): 
            if inputArray[i] % jump_distance == 0: 
                obstacle_suc = True
                break
    return jump_distance 