def convertFive(n):
    for i in n:
        if i == '0':
            print('5', end = '')
        else:
            print(i, end = '')

print(convertFive('121'))