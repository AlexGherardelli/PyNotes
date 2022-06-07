def to_binary(n, result=""):
    # base case: n == 0
    if n == 0:
        return result

    result = str(n % 2) + result
    return to_binary(n // 2, result)


print(to_binary(10))
