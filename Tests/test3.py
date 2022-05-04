
# counter = 0

# def dig(counter):
#     if counter < 50:
#         counter += 1
#     else:
#         quit()
#     print(counter)
#     dig(counter)

# dig(counter)

# def subString(Str,n):
#     for Len in range(1,n + 1):
#         for i in range(n - Len + 1):
#             j = i + Len - 1
#             for k in range(i,j + 1):
#                 print(Str[k],end="")
#             print()


# Algorithm with grade O(1)
def o_one(num):
    return num[0]

# Algorithm with grade O(log n)
def o_log_n(num, searchable):
    low = 0
    high = len(num) - 1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if num[mid] < searchable:
            low = mid + 1
        elif num[mid] > searchable:
            high = mid - 1
        else:
            return mid
    return -1

# Algorithm with grade O(n)
def o_n(num):
    return [2*x for x in num]

# Algorithm with grade O(nᶜ)
def o_nc(num):
    return [[x+inner_num for x in num] for inner_num in num]

# -------------------------------------------------------------------------------------------------

# Grade O(1) - Iterates once and returns the number
print(o_one([1, 2, 3]))

# Grade O(log n) - Iterates more then once and less then len(list) and returns searchable number
print(o_log_n([1, 2, 3], 2))

# Grade O(n) - Iterates over the whole list and returns a value for each value in list
print(o_n([1, 2, 3]))

# Grade O(nᶜ) - Iterating over the list for each element in the list?
print(o_nc([1, 2, 3]))