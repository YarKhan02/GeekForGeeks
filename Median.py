def median(arr):
    arr = sorted(arr)
    size = len(arr)
    middle = size // 2

    if size % 2 != 0:
        return arr[middle]
    
    else:
        mid_value = (arr[middle - 1] + arr[middle]) // 2
        return mid_value


print(median([1, 2, 3, 4, 5]))