def binarySearch():
    n = int(input())
    arr = [int(x) for x in input().split()]
    k = int(input())

    low = 0
    high = len(arr) - 1

    while low <= high:
        midIndex = (low + high) // 2

        if arr[midIndex] == k:
            return midIndex

        elif arr[midIndex] < k:
            low = midIndex + 1

        else:
            high = midIndex - 1

    return -1

print(binarySearch())