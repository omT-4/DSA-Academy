# # print(6 % 4)
# def matrix_search(matrix, target):
#     rows = len(matrix)
#     columns = len(matrix[0])
#     left = 0
#     right = rows * columns - 1
#     while left <= right:
#         mid = (left + right) // 2
#         row = mid // columns 
#         column = mid % columns
#         if matrix[row][column] == target:
#             return True
#         elif matrix[row][column] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return False


def matrix_search(matrix, target):
    rows = len(matrix)
    columns = len(matrix[1])
    left = 0
    right = rows * columns - 1

    while left <= right:
        mid = (left + right) // 2

        row = mid // columns
        column = mid % columns

        if matrix[row][column] == target:
            return True
        elif matrix[row][column] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

print(matrix_search(matrix, 16))  # Expected: True
print(matrix_search(matrix, 1))   # Expected: True
print(matrix_search(matrix, 60))  # Expected: True
print(matrix_search(matrix, 13))  # Expected: False
print(matrix_search(matrix, 0))   # Expected: False
print(matrix_search(matrix, 70))  # Expected: False
