def findIndex(n, k):
    index = 0

    if len(n) > 1:
        return -1

    while index < len(n):
        if n[index] == k:
            print(index, end = ' ')