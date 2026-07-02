def is_diagonal_same(matrix):

    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(1, rows):
        for j in range(1, cols):

            if matrix[i][j] != matrix[i-1][j-1]:
                return False

    return True


# Test Cases
matrix1 = [
    [42, 7, 13, 99],
    [6, 42, 7, 13],
    [1, 6, 42, 7]
]

matrix2 = [
    [8, 23],
    [69, 1]
]

print(is_diagonal_same(matrix1))  # True
print(is_diagonal_same(matrix2))  # False