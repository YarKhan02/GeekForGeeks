def sum(n, count = 0):
    if n < 1:
        return count

    count += n

    return sum(n - 1, count)

    ans = n*(n + 1)//2

print(sum(100))

        