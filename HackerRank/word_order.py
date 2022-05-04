

dict = {}
repeater = input()
counter = 0
answer = ""
while counter < int(repeater):
    n = input()
    cleaned_word = n.strip("\n")
    if cleaned_word in dict.keys():
        dict[cleaned_word] += 1
    else:
        dict[cleaned_word] = 1
    counter += 1

for keys, values in dict.items():
    answer += str(values) + " "



print(f"{len(dict.keys())}")
print(f"{answer}")
