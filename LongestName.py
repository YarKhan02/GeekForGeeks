def longestElement(names):
    index = 0
    longest = ''

    while index <= len(names) - 1:
        if len(names[index]) > len(longest):
            longest = names[index]

        index += 1

    return longest

print(longestElement(["Geek", "Geeks", "Geeksfor",
  "GeeksforGeek", "GeeksforGeeks"]))