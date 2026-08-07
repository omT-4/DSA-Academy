# Second Largest Element

## Problem

Find the second distinct largest element in a single traversal.

Example:

```python
numbers = [12, 45, 30, 50, 20]
```

Output:

```
45
```

---

# Intuition

Maintain two ordered values:

- `largest`
- `second_largest`

Whenever a new largest is found:

- Save the old largest as `second_largest`.
- Update `largest`.

Otherwise, if the current number is greater than `second_largest` and different from `largest`, update `second_largest`.

---

# Algorithm

1. Initialize:
   - `largest = numbers[0]`
   - `second_largest = float("-inf")`
2. Traverse the array once.
3. If a new largest is found:
   - Move the old largest to `second_largest`.
   - Update `largest`.
4. Otherwise, update `second_largest` if appropriate.
5. Print the answer.

---

# Code

```python
numbers = [12, 45, 30, 50, 20]

largest = numbers[0]
second_largest = float("-inf")

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num

    elif num > second_largest and num != largest:
        second_largest = num

print(second_largest)
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
Only three variables are maintained.

---

# Common Mistakes

- Updating `largest` before saving it.
- Initializing `second_largest` with `0`.
- Forgetting `num != largest`.
- Using sorting when a single traversal is enough.

---

# Pattern Recognition

Traversal

↓

Comparison Pattern

↓

Maintain Ordered Values

---

# Key Takeaways

- Save the old largest before overwriting it.
- Use `float("-inf")` as the initial sentinel.
- Maintain state throughout the traversal.
- Time: O(n)
- Space: O(1)