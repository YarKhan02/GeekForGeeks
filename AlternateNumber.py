def alternate(n):
    length = len(n)
    index = 0

    while index < length:
        if index % 2 == 0:
            print(n[index], end = ' ')

        index += 1

print(alternate([1, 2, 3, 4, 5]))
