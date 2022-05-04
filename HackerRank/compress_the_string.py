"""https://stackoverflow.com/questions/773/how-do-i-use-itertools-groupby"""

from itertools import groupby

n = input()

answer_list = []
for key, group in groupby(n):
    answer_list.append("(" + str(len(list(group))) + ", " + key + ") ")

print("".join(answer_list))
