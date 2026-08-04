# Finding the Largest Element

## Problem

Given an array, find the largest element.

Example:

```python
numbers = [12, 45, 8, 31, 19]
```

Output:

```
45
```

---

# Intuition

Assume the first element is the largest.

Compare every remaining element with the current largest.

If a larger element is found, update the largest.

Continue until the last element.

---

# Algorithm

1. Assume the first element is the largest.
2. Traverse the array.
3. Compare each element with the current largest.
4. If the current element is larger, update the largest.
5. Print the largest element.

---

# Code

```python
numbers = [12, 45, 8, 31, 19]

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print(largest)
```

---

# Dry Run

Initial

```
largest = 12
```

Iteration 1

```
num = 12

12 > 12

False
```

Iteration 2

```
num = 45

45 > 12

True

largest = 45
```

Iteration 3

```
8 > 45

False
```

Iteration 4

```
31 > 45

False
```

Iteration 5

```
19 > 45

False
```

Output

```
45
```

---

# Memory Model

Variables:

- numbers
- largest
- num

Only `largest` changes when a larger value is found.

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

Only two extra variables (`largest` and `num`) are used.

---

# Common Mistakes

❌ Initialize with `0`.

❌ Initialize with an arbitrary number.

❌ Sort the array first.

---

# Interview Tip

Initialize using:

```python
largest = numbers[0]
```

because it is guaranteed to be a valid element in the input.

---

# Concept Connection

```
Problem Solving
        │
        ▼
Arrays
        │
        ▼
Traversal
        │
        ▼
Comparison
        │
        ▼
Initialization
        │
        ▼
Largest Element
```

# Key Takeaways

- Initialize with the first element.
- Traverse the array once.
- Update the largest when a bigger value is found.
- Time Complexity = O(n)
- Space Complexity = O(1)