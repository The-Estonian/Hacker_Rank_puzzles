def diagonalDifference(arr):
    first_diagonal = 0
    second_diagonal = 0
    counter = 0
    max_counter = len(arr)-1

    for _ in range(len(arr)):
        first_diagonal += arr[counter][counter]
        second_diagonal += arr[max_counter][counter]
        counter += 1
        max_counter -= 1
        print(first_diagonal, second_diagonal)
    return abs(first_diagonal-second_diagonal)



print(diagonalDifference([[11, 2, 4, 8], [4, 5, 6, -1], [10, 2, 8, -12], [4, 9, 5, 6]]))