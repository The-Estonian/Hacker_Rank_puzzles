
def lonelyinteger(a):
    dict = {}
    for key in a:
        if key in dict.keys():
            dict[key] += 1
        else:
            dict[key] = 1

    for key, value in dict.items():
        if value == 1:
            return key

print(lonelyinteger([34, 95, 34, 64, 45, 95, 16, 80, 80, 75, 3, 25, 75, 25, 31, 3, 64, 16, 31]))