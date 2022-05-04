n = input()
even_digit = []
odd_digit = []
capital_list = []
lower_list = []
for _ in n:
    if _.islower():
        lower_list.append(_)
    elif _.isupper():
        capital_list.append(_)
    elif _.isnumeric():
        if int(_)%2 == 0:
            even_digit.append(_)
        else:
            odd_digit.append(_)

capital_list.sort()
lower_list.sort()
even_digit.sort()
odd_digit.sort()

answer = "".join(lower_list)
answer = answer + "".join(capital_list)
answer = answer + "".join(odd_digit)
answer = answer + "".join(even_digit)

print(answer)
