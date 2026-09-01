def search_matrix(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])

    row = 0
    column = columns - 1

    while row < rows and column >= 0:
        current = matrix[row][column]

        if current == target:
            return True
        elif current > target:
            column -= 1
        else:
            row += 1

    return False

matrix = [
    [1,  4,  7, 11, 15],
    [2,  5,  8, 12, 19],
    [3,  6,  9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(search_matrix(matrix, 14))  # Expected: True
print(search_matrix(matrix, 1))   # Expected: True
print(search_matrix(matrix, 30))  # Expected: True
print(search_matrix(matrix, 13))  # Expected: True
print(search_matrix(matrix, 18))  # Expected: True

print(search_matrix(matrix, 20))  # Expected: False
print(search_matrix(matrix, 0))   # Expected: False
print(search_matrix(matrix, 31))  # Expected: False