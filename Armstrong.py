def armstrong(s):
    count = 0

    for i in s:
        i = int(i)
        count += i*i*i

    s = int(s)

    if count == s:
        return 'Yes'

    return 'No'

print(armstrong('371'))