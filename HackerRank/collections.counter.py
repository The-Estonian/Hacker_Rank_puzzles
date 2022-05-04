from collections import Counter

n = input()
N = input()
N = N.split()
my_dict = Counter(N)
customer = input()
payday = 0
for customers in range(int(customer)):
    order = input()
    order = order.split()
    item = order[0]
    price = int(order[1])
    if item in my_dict.keys():
        if my_dict[item] > 1:
            my_dict[item] -= 1
            payday += price
        elif my_dict[item] == 1:
            del my_dict[item]
            payday += price
        else:
            pass
print(payday)