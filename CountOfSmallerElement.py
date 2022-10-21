def countOfElements(a, x):
    count = 0

    for i in a:
        if i <= x:
            count += 1

    return count

print(countOfElements([1, 2, 4, 5, 8, 10], 9))
