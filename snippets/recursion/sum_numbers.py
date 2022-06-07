# -*- coding: utf-8 -*-

def sum_numbers(n):
    if n == 1:
        return 1
    else:
        return n + sum_numbers(n - 1)


def sum_numbers_iteratively(n):
    result = 0
    for i in range(n + 1):
        result += i
    return result


n = 10
print(f"Sum iteratively until {n} :  {sum_numbers_iteratively(n)}")

print(f"Sum recursively until {n} :  {sum_numbers(n)}")
