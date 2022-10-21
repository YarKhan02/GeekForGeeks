def valueEqualToIndex(arr):
    index = 0
    count = []
    x = 1

    while index <= len(arr) - 1:
        if x == arr[index]:
            count.append(x)
        
        index += 1
        x += 1

    return count


print(valueEqualToIndex([625, 538, 549, 484, 596, 42, 603, 351, 292, 10]))