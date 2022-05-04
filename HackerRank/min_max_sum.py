def miniMaxSum(arr):
    if arr[0] == arr[1] and arr[1] == arr[2] and arr[2] == arr[3] and arr[3] == arr[4]:
        print((arr[0]*4), (arr[0]*4))
    else:
        max_value = 0
        for _ in arr:
            if _ > max_value:
                max_value = _

        min_value = max_value
        for _ in arr:
            if _ < min_value:
                min_value = _

        min_sum = 0
        max_sum = 0

        for _ in arr:
            if _ == min_value:
                pass
            else:
                max_sum += _

        for _ in arr:
            if _ == max_value:
                pass
            else:
                min_sum += _

        print(min_sum, max_sum)
    
