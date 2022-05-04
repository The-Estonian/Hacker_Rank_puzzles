
def plusMinus(arr):
    count = len(arr)
    positive = 0
    negative = 0
    neutral = 0
    for _ in arr:
        if _ > 0:
            positive += 1
        elif _ < 0:
            negative += 1
        else:
            neutral += 1
    if positive == 0:
        positive_return = format(0, ".6f")
    else:
        positive_return = 1/(count/positive)
        positive_return = format(positive_return, ".6f")

    if negative == 0:
        negative_return = format(0, ".6f")
    else:
        negative_return = 1/(count/negative)
        negative_return = format(negative_return, ".6f")

    if neutral == 0:
        neutral_return = format(0, ".6f")
    else:
        neutral_return = 1/(count/neutral)
        neutral_return = format(neutral_return, ".6f")

    print(positive_return)
    print(negative_return)
    print(neutral_return)


plusMinus([1, 3, 5, 6, 4, 1])