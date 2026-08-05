# Reverse Array (Two Pointers Pattern)

## Problem

Reverse an array **in-place** using the Two Pointers technique.

Example:

```python
numbers = [1, 2, 3, 4, 5]
```

Output:

```text
[5, 4, 3, 2, 1]
```

---

# Intuition

Use two pointers:

- Left starts at the beginning.
- Right starts at the end.

Swap their values.

Move both pointers toward the center.

Stop when the pointers meet or cross.

---

# Algorithm

1. Initialize `left = 0`.
2. Initialize `right = len(numbers) - 1`.
3. While `left < right`:
   - Swap `numbers[left]` and `numbers[right]`.
   - Increment `left`.
   - Decrement `right`.
4. Print the reversed array.

---

# Code

```python
numbers = [1, 2, 3, 4, 5]

left = 0
right = len(numbers) - 1

while left < right:
    temp = numbers[left]
    numbers[left] = numbers[right]
    numbers[right] = temp

    left += 1
    right -= 1

print(numbers)
```

---

# Dry Run

Initial

```
[1,2,3,4,5]

left = 0
right = 4
```

Iteration 1

```
Swap 1 ↔ 5

[5,2,3,4,1]

left = 1
right = 3
```

Iteration 2

```
Swap 2 ↔ 4

[5,4,3,2,1]

left = 2
right = 2
```

Condition

```
left < right

2 < 2

False
```

Stop.

---

# Memory Model

Variables:

- numbers
- left
- right
- temp

The array changes after every swap.

Pointers move toward the center.

---

# Time Complexity

```
O(n)
```

Reason:

Each element is visited at most once.

---

# Space Complexity

```
O(1)
```

Reason:

Only three extra variables are used.

---

# Common Mistakes

❌ Forgetting to move the pointers.

❌ Using `a = b; b = a`.

❌ Using another array unnecessarily.

❌ Using `while True`.

---

# Interview Tip

The Two Pointers approach is preferred because it reverses the array **in-place** using constant extra space.

---

# Pattern Recognition

This is the **Two Pointers Pattern**.

Instead of moving one variable through the array, two pointers move toward each other while solving the problem.

---

# Concept Connection

```
Traversal
     │
     ▼
Comparison
     │
     ▼
Search
     │
     ▼
Accumulation
     │
     ▼
Counting
     │
     ▼
Two Pointers
     │
     ▼
Reverse Array
```

# Key Takeaways

- Use two pointers.
- Swap elements.
- Move pointers inward.
- Stop when `left >= right`.
- Time Complexity = O(n)
- Space Complexity = O(1)