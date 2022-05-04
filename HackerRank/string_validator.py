data_string = input()
alphanum = False
alphabet = False
digits = False
lower_case = False
upper_case = False
for _ in data_string:
    if _.isalpha():
        alphabet = True
    if _.isdigit():
        digits = True
    if _.islower():
        lower_case = True
    if _.isupper():
        upper_case = True
if alphabet == True or digits == True:
    alphanum = True

print(alphanum)
print(alphabet)
print(digits)
print(lower_case)
print(upper_case)

