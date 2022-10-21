def swapKth(arr, k):
    n = len(arr)
    end = n - k

    temp = 0

    temp = arr[k - 1]
    arr[k - 1] = arr[end]
    arr[end] = temp

    return arr

print(swapKth([1, 2, 3, 4, 5, 6], 2))