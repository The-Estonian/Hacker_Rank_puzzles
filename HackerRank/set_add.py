n = input()
list = []
for i in range(int(n)):
    data = input()
    list.append(data)
setter = set(list)
print(len(setter))