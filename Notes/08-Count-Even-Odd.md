# Count Even and Odd Numbers

## Problem

Given an array, count how many even and odd numbers it contains.

Example:

```python
numbers = [4, 7, 10, 3, 8, 6]
```

Output:

```
Even = 4
Odd = 2
```

---

# Intuition

Start with two counters:

- even_count = 0
- odd_count = 0

Visit every element.

If the number is even, increase `even_count`.

Otherwise, increase `odd_count`.

---

# Algorithm

1. Initialize `even_count = 0` and `odd_count = 0`.
2. Traverse the array.
3. Check if the current number is even using `%`.
4. Increase the appropriate counter.
5. Print both counters.

---

# Code

```python
numbers = [4, 7, 10, 3, 8, 6]

even_count = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even:", even_count)
print("Odd:", odd_count)
```

---

# Dry Run

Initial State

```
even_count = 0
odd_count = 0
```

Iteration 1

```
num = 4

4 % 2 = 0

True

even_count = 1
```

Iteration 2

```
num = 7

7 % 2 = 1

False

odd_count = 1
```

Continue until the last element.

Final Output

```
Even = 4
Odd = 2
```

---

# Memory Model

Variables:

- numbers
- even_count
- odd_count
- num

`num` changes every iteration.

The counters increase whenever their condition is satisfied.

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

Only a fixed number of variables are used.

---

# Common Mistakes

❌ Using `/` instead of `%`.

❌ Forgetting to initialize counters to `0`.

❌ Increasing the wrong counter.

---

# Interview Tip

The `%` operator returns the remainder.

- `num % 2 == 0` → Even
- `num % 2 != 0` → Odd

---

# Pattern Recognition

Counting is an extension of the Accumulation Pattern.

Instead of maintaining one running total, we maintain one or more running counters.

---

# Concept Connection

```
Traversal
     │
     ▼
Accumulation
     │
     ▼
Counting
     │
     ├──────────────┐
     │              │
     ▼              ▼
Even Count     Odd Count
```

# Key Takeaways

- Initialize counters to `0`.
- Use `%` to check even and odd numbers.
- Increase the correct counter.
- Time Complexity = O(n)
- Space Complexity = O(1)