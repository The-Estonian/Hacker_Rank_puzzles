def average(array):
    # your code goes here
    list = []
    for x in array:
        list.append(int(x))
    return round(sum(set(list))/len(set(list)), 3)

