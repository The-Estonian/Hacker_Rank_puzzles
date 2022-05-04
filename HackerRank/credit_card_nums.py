

def starts_with(number):
    if number[0] == "4" or number[0] == "5" or number[0] == "6":
        return True

def number_count(number):
    if len(number) == 16 or number[4] == "-" and number[9] == "-" and number[14] == "-" and len(number) == 19:
        return True

def only_numbers(number):
    not_numeric = 0
    for _ in number:
        if _.isnumeric() or _ == "-":
            pass
        else:
            not_numeric = 1
    if not_numeric == 1:
        return False
    else:
        return True

def card_repetition(number):
    repetition_found = 0
    counter = 1
    index = 1
    list = []
    for _ in number:
        if _.isnumeric():
            list.append(_)
        else:
            pass
    for num in range(len(list)-1):
        if list[index-1] == list[index]:
            counter += 1
        else:
            counter = 1
        index += 1
        if counter == 4:
            repetition_found = 1
    if repetition_found == 1:
        return False
    else:
        return True


n = input()
for cards in range(int(n)):
    validate = 0
    eradicate_card = 0
    credit_card = input()

    if starts_with(credit_card):
        validate = 1
    else:
        eradicate_card = 1
    
    if number_count(credit_card):
        validate = 1
    else:
        eradicate_card = 1

    if only_numbers(credit_card):
        validate = 1
    else:
        eradicate_card = 1
    
    if card_repetition(credit_card):
        validate = 1
    else:
        eradicate_card = 1

    if validate == 1 and eradicate_card == 0:
        print("Valid")
    else:
        print("Invalid")









