# Finding the Smallest Element

## Problem

Given an array, find the smallest element.

Example:

```python
numbers = [12, 45, 8, 31, 19]
```

Output:

```
8
```

---

# Intuition

Assume the first element is the smallest.

Compare every remaining element with the current smallest.

If a smaller element is found, update the smallest.

Continue until the last element.

---

# Algorithm

1. Assume the first element is the smallest.
2. Traverse the array.
3. Compare each element with the current smallest.
4. If the current element is smaller, update the smallest.
5. Print the smallest element.

---

# Code

```python
numbers = [12, 45, 8, 31, 19]

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print(smallest)
```

---

# Dry Run

Initial

```
smallest = 12
```

Iteration 1

```
num = 12

12 < 12

False
```

Iteration 2

```
num = 45

45 < 12

False
```

Iteration 3

```
num = 8

8 < 12

True

smallest = 8
```

Iteration 4

```
31 < 8

False
```

Iteration 5

```
19 < 8

False
```

Output

```
8
```

---

# Memory Model

Variables:

- numbers
- smallest
- num

Only `smallest` changes when a smaller value is found.

`num` changes every iteration.

---

# Time Complexity

```
O(n)
```

Reason:

Every element is visited once.

---

# Space Complexity

```
O(1)
```

Reason:

Only two extra variables (`smallest` and `num`) are used.

---

# Common Mistakes

❌ Initialize with `0`.

❌ Initialize with an arbitrary number.

❌ Sort the array first.

---

# Interview Tip

Initialize using:

```python
smallest = numbers[0]
```

because it is guaranteed to be a valid element in the input.

---

# Pattern Recognition

The Smallest Element algorithm is the same comparison pattern as the Largest Element algorithm.

Only these changes are required:

- `largest` → `smallest`
- `>` → `<`

Everything else remains the same.

---

# Concept Connection

```
Traversal
      │
      ▼
Comparison Pattern
     /       \
    ▼         ▼
Largest   Smallest
```

# Key Takeaways

- Initialize with the first element.
- Traverse the array once.
- Update the smallest when a smaller value is found.
- Time Complexity = O(n)
- Space Complexity = O(1)