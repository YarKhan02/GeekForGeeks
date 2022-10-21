def mul(arr):
    count = 1

    for i in arr:
        count *= i

    return count


print(mul([1, 2, 3, 4, 5]))