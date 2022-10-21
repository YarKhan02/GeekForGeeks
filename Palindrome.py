def palindrome(n):
    n = str(n)
    length = len(n)
    if length < 2:
        return 'Yes'

    if n[0] == n[length - 1]:
        return palindrome(n[1: length - 1])

    return 'No'

print(palindrome(123))