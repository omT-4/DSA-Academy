# Sum of Array Elements

## Problem

Given an array, calculate the sum of all elements.

Example:

```python
numbers = [15, 20, 10, 5]
```

Output:

```
50
```

---

# Intuition

Start with a total of `0`.

Visit each element one by one.

Add the current element to the running total.

After the last element, the running total is the answer.

---

# Algorithm

1. Initialize `total = 0`.
2. Traverse the array.
3. Add the current element to `total`.
4. Repeat until the last element.
5. Print `total`.

---

# Code

```python
numbers = [15, 20, 10, 5]

total = 0

for num in numbers:
    total = total + num

print(total)
```

---

# Dry Run

Initial State

```
total = 0
```

Iteration 1

```
num = 15

0 + 15 = 15

total = 15
```

Iteration 2

```
num = 20

15 + 20 = 35

total = 35
```

Iteration 3

```
num = 10

35 + 10 = 45

total = 45
```

Iteration 4

```
num = 5

45 + 5 = 50

total = 50
```

Output

```
50
```

---

# Memory Model

Variables:

- numbers
- total
- num

`num` changes every iteration.

`total` stores the running sum.

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

Only two extra variables (`total` and `num`) are used.

---

# Common Mistakes

❌ Initialize `total = 1`.

❌ Write `total = num` instead of `total = total + num`.

❌ Forget to update the total inside the loop.

---

# Interview Tip

Initialize `total = 0` because **0 is the identity element of addition**.

---

# Pattern Recognition

This is the **Accumulation Pattern**.

Instead of remembering the best value, we maintain a **running total**.

---

# Concept Connection

```
Traversal
     │
     ├──────────────┐
     │              │
     ▼              ▼
Comparison      Search
     │              │
     ▼              ▼
Largest      Linear Search
Smallest
     │
     ▼
Accumulation
     │
     ▼
Running Total
```

# Key Takeaways

- Initialize `total = 0`.
- Keep a running total.
- Visit every element once.
- Time Complexity = O(n)
- Space Complexity = O(1)