def is_palindrome(string):
    # base case: the string is less than 1 character
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])

    return False


""" print(f"kayak : {is_palindrome("kayak")}")
print(f"empty string : {is_palindrome("")}")
print(f"a : {is_palindrome("a")}")
print(f"alessandra : {is_palindrome("alessandra")}")
 """

print(is_palindrome("racecar"))
