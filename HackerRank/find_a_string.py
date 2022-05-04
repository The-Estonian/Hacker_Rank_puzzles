

def count_substring(string, sub_string):
    counter = 0
    first_index = 0
    second_index = len(sub_string)
    for i in range(len(string)):
        if sub_string in string[first_index:second_index]:
            counter += 1
            first_index += 1
            second_index += 1
        else:
            first_index += 1
            second_index += 1
    return counter


print(count_substring("ABCDCDC", "CDC"))