# Lesson 22 - Search in a 2D Matrix II

## Core Idea

The matrix is sorted from left to right in every row and top to bottom in every column, but it cannot be treated as one continuous sorted 1D array.

Start at the top-right corner and use the current value to eliminate an entire row or column.

---

## Starting Position

```python
row = 0
column = columns - 1
Top-right corner.

Search Logic
Current value == target
return True
Target found.
Current value > target
Move LEFT:
column -= 1
Everything below the current value is greater, so the current column can be eliminated.
Current value < target
Move DOWN:
row += 1
Everything to the left of the current value is smaller, so that part of the current row can be eliminated.

Boundary Condition
while row < rows and column >= 0:
Continue searching while the current position is inside the matrix.
If:
row == rows
we have moved below the matrix.
If:
column == -1
we have moved outside the matrix on the left.
In either case, the target was not found.

Algorithm
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

Important Rules
- Start at the top-right corner.
- current > target → move LEFT.
- current < target → move DOWN.
- current == target → return True.
- Leaving the matrix → return False.

Complexity
For an m × n matrix:
- Time Complexity: O(m + n)
- Space Complexity: O(1)
Each move eliminates a row or a column.