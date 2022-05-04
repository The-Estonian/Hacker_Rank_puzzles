def findMedian(arr):
    arr.sort()
    counter = len(arr)+1
    return arr[round(counter/2)-1]