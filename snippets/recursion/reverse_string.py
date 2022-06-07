def reverse(string):
    # base case: string is empty
    if string == "":
        return ""
    else:
        return string[-1] + reverse(string[:-1])


print(reverse("hello"))
print(reverse("Alessandra"))