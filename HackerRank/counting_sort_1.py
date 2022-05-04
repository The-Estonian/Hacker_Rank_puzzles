
def countingSort(arr):
    dict = {}
    for keys in range(100):
        dict[keys] = 0
    
    for key in arr:
        if key in dict.keys():
            dict[key] += 1
            
    filled_array = []    
    for key, value in dict.items():
        filled_array.append(value)
    return filled_array

countingSort([1, 2, 3])

