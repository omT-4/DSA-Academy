# Frequency Count

## Problem

Count how many times each element appears in an array.

Example:

```python
numbers = [2, 5, 2, 8, 5, 2]
```

Output:

```
{
    2: 3,
    5: 2,
    8: 1
}
```

---

# Intuition

Traverse the array once.

For every element:

- If it already exists in the dictionary, increase its count.
- Otherwise, create a new key with count `1`.

---

# Algorithm

1. Create an empty dictionary.
2. Traverse the array.
3. Check whether the current element exists.
4. Update its count or create a new key.
5. Print the dictionary.

---

# Code

```python
numbers = [2, 5, 2, 8, 5, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)
```

---

# Time Complexity

O(n)

Reason:
Visit each element once.

---

# Space Complexity

O(n)

Reason:
In the worst case, every element is unique, so the dictionary grows with the input.

---

# Common Mistakes

- Forgetting to create a key before increasing its count.
- Using variables instead of a dictionary.
- Thinking dictionaries preserve insertion order for solving the algorithm (the algorithm does not depend on order).

---

# Pattern Recognition

Traversal

↓

Counting Pattern

↓

Dictionary (Key → Count)

---

# Key Takeaways

- Dictionaries store key-value pairs.
- Keys are unique.
- Values can be updated.
- Frequency counting is a reusable interview pattern.