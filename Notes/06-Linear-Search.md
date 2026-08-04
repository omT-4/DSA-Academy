# Linear Search

## Problem

Given an array and a target value, determine whether the target exists in the array.

Example:

```python
numbers = [15, 8, 27, 10, 35]
target = 10
```

Output:

```
Element Found
```

---

# Intuition

Start from the first element.

Compare each element with the target.

If the target is found, stop immediately.

If the loop finishes without finding the target, the element does not exist.

---

# Algorithm

1. Assume the target has not been found.
2. Traverse the array.
3. Compare each element with the target.
4. If the target is found:
   - Update the flag.
   - Exit the loop using `break`.
5. Print whether the element was found.

---

# Code

```python
numbers = [15, 8, 27, 10, 35]

target = 10

found = False

for num in numbers:
    if num == target:
        found = True
        break

if found:
    print("Element Found")
else:
    print("Element Not Found")
```

---

# Dry Run

Initial State

```
target = 10

found = False
```

Iteration 1

```
15 == 10

False
```

Iteration 2

```
8 == 10

False
```

Iteration 3

```
27 == 10

False
```

Iteration 4

```
10 == 10

True

found = True

break
```

Loop stops immediately.

Output

```
Element Found
```

---

# Memory Model

Variables:

- numbers
- target
- found
- num

`num` changes every iteration.

`found` changes only when the target is found.

---

# Best Case

Target is the first element.

```
O(1)
```

---

# Worst Case

Target is the last element or not present.

```
O(n)
```

---

# Average Case

Target is usually found somewhere in the middle.

```
O(n)
```

---

# Space Complexity

```
O(1)
```

Reason:

Only a fixed number of variables are used.

---

# Common Mistakes

❌ Forgetting `break`.

❌ Using `=` instead of `==`.

❌ Initializing `found = True`.

---

# Interview Tip

Use `break` because once the target is found, further comparisons are unnecessary.

---

# Concept Connection

```
Traversal
      │
      ▼
Comparison
      │
      ▼
Decision
      │
      ▼
Target Found?
     /      \
   Yes       No
    │         │
    ▼         ▼
 break    Continue
```

---

# Key Takeaways

- Linear Search checks elements one by one.
- It can stop early using `break`.
- Best Case = O(1)
- Worst Case = O(n)
- Space Complexity = O(1)