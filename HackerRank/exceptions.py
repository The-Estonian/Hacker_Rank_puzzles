# Exceptions

N = input()
for x in range(int(N)):
    data = input()
    data = data.split()
    try:
        print(int(int(data[0])/int(data[1])))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as e:
        print(f"Error Code: {e}")
