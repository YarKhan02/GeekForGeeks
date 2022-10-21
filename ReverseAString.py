def reverse(string):
    length = len(string)

    if length == 0:
        return ''

    print(string[length - 1], end = '')

    return reverse(string[0: length - 1])

print(reverse('GeeksforGeeks'))