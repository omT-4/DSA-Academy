# Lesson 21 - Search in a 2D Matrix

## Core Idea

A specially sorted 2D matrix can be treated as a virtual 1D sorted array.

We can apply Binary Search without actually converting the matrix into a separate 1D array.

---

## Matrix Properties

Binary Search is possible when:

1. Every row is sorted from left to right.
2. The first element of each row is greater than the last element of the previous row.

Example:

[1,  3,  5,  7]
[10, 11, 16, 20]
[23, 30, 34, 60]

Can be treated as:

[1, 3, 5, 7, 10, 11, 16, 20, 23, 30, 34, 60]

---

## Virtual Index to Matrix Position

For a virtual index:

```python
row = mid // columns
column = mid % columns

Example:
mid = 6
columns = 4

row = 6 // 4 = 1
column = 6 % 4 = 2

matrix[1][2] = 16

Binary Search Boundaries
left = 0
right = rows * columns - 1
The Binary Search runs over the total number of elements.

Algorithm
def matrix_search(matrix, target):
    rows = len(matrix)
    columns = len(matrix[0])

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

Important Rules
- Treat the matrix as a virtual 1D sorted array.
- row = mid // columns
- column = mid % columns
- If middle value is smaller than target, search right.
- If middle value is greater than target, search left.
- Return True if found, otherwise False.

Complexity
For a matrix with m rows and n columns:
- Time Complexity: O(log(m × n))
- Space Complexity: O(1)

