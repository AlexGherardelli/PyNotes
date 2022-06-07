def search(lst, x, left=0, right=0):
    left, right = 0, len(lst) - 1
    mid = (left + right) // 2
    lst.sort()

    if x == lst[mid]:
        return True
    elif x < lst[mid]:
        # keep searching on the left
        pass
    elif x > lst[mid]:
        # keep searchign on the right
        pass

    return False


lst = [10, 50, 32, 24, 66, 124, 0, 12]
x = 10

print(search(lst, x))
