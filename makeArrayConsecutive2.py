def makeArrayConsecutive2(statues):
    
    max_height = max(statues)
    min_height = min(statues)
    array_length  = len(statues)
    count_of_element = max_height - min_height + 1
    return count_of_element-array_length

print(makeArrayConsecutive2([1, 2, 3, 10, 11, 15]))


# def makeArrayConsecutive2(statues):
#     return max(statues)-min(statues)-len(statues)+1