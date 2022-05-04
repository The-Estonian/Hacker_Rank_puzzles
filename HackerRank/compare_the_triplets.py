
def compareTriplets(a, b):
    # Write your code here
    first = 0
    second = 0
    if a[0] > b[0]:
        first += 1
    elif a[0] < b[0]:
        second += 1
    else:
        pass

    if a[1] > b[1]:
        first += 1
    elif a[1] < b[1]:
        second += 1
    else:
        pass

    if a[2] > b[2]:
        first += 1
    elif a[2] < b[2]:
        second += 1
    else:
        pass

    return first, second
