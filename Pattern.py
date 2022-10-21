def pattern(n):
    for i in range(0, n):
        for j in range(n, 0, -1):
            for k in range(n, i, -1):
                print(j, end = ' ')
        print('$', end = '')

print(pattern(3))