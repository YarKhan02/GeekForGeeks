def binary(str):
    index = 0
    
    while index <= len(str) - 1:

        if str[index] == '1' or str[index] == '0':
            index += 1 

        else:
            return False

    return True

print(binary('75'))