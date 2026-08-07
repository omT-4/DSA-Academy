# Find Maximum and Minimum Together

## Problem

Find both the largest and smallest element in a single traversal.

Example:

```python
numbers = [25, 10, 35, 5, 18]
```

Output:

```
Largest = 35
Smallest = 5
```

---

# Intuition

Instead of traversing the array twice, visit each element once.

For every element:

1. Compare with the current largest.
2. Compare with the current smallest.

Update only when required.

---

# Algorithm

1. Initialize:
   - `largest = numbers[0]`
   - `smallest = numbers[0]`
2. Traverse the array once.
3. Compare each element with `largest`.
4. Compare the same element with `smallest`.
5. Print both values.

---

# Code

```python
numbers = [25, 10, 35, 5, 18]

largest = numbers[0]
smallest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
```

---

# Time Complexity

O(n)

Reason:
One traversal of the array.

---

# Space Complexity

O(1)

Reason:
Only `largest`, `smallest`, and `num` are used.

---

# Common Mistakes

- Initializing with `0`.
- Using `if...else` instead of two independent `if` statements.
- Traversing the array twice.

---

# Pattern Recognition

Traversal

↓

Comparison Pattern

↓

Multiple Comparisons in One Traversal

---

# Key Takeaways

- Use `numbers[0]` for initialization.
- Ask two independent comparison questions.
- One traversal can solve multiple tasks.
- Time: O(n)
- Space: O(1)