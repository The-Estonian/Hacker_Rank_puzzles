#string formatting
def print_formatted(number):
    counter = 1
    for _ in range(int(number)):
        octa_counter = oct(counter)
        hex_counter = hex(counter)
        binary_counter = bin(counter)
        a = counter
        b = octa_counter[2:]
        c = hex_counter[2:]
        c = c.upper()
        d = binary_counter[2:]

        
        space_counter = int(len(bin(number)))

        a_space = space_counter-int(len(str(counter))+2)
        b_space = space_counter-int(len(str(octa_counter)))
        c_space = space_counter-int(len(str(hex_counter)))
        d_space = space_counter-int(len(str(binary_counter)))

        empty_space = " "
        print(f"{empty_space*a_space}{a} {empty_space*b_space}{b} {empty_space*c_space}{c} {empty_space*d_space}{d}")

        counter += 1
