from math import remainder


def rem(num1, num2):
    if num1 < num2:
        return num1

    result = num1 % num2

    return result

print(rem(5, 10))