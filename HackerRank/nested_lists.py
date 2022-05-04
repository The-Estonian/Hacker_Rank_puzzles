
# N = input()
# nested_list = []
# for _ in range(int(N)):
#     list = []
#     name = input()
#     score = float(input())
#     list.append(name)
#     list.append(score)
#     nested_list.append(list)
# print(nested_list)

nested_list = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
nested_list.sort(key = lambda x: x[1])
winner = None
winner = nested_list[0]
for items in nested_list:
    if winner[1] < items[1]:
        winner = items
    elif winner[1] == items[1]:
        winner = winner + items
    
print(nested_list)
print(winner)