def search(lst, x, left=0, right=0):
    left, right = 0, len(lst) - 1
    mid = (len(lst) - 1) // 2
    try:

        if x == lst[mid]:
            return True

        if x < lst[mid]:
            return search(lst[:mid], x, left, right=mid)
        # keep searching on the left
        if x > lst[mid]:
            # keep searchign on the right
            return search(lst[mid:], x, left=mid, right=len(lst) + 1)

        return False
    except IndexError:
        return False


lst = [10, 50, 32, 24, 66, 124, 0, 12]
lst.sort()


for x in lst:
    print(search(lst, x))
