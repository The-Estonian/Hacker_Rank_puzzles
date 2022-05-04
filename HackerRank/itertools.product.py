from itertools import product


A = input()
A = A.split()
B = input()
B = B.split()


C = list(product(A, B))
list = [", ".join(x) for x in C]
list = ["("+x+")" for x in list]
word = " ".join(list)

print(word)
