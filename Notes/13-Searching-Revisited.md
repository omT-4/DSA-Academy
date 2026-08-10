# Searching Revisited

## What is Searching?

Searching means finding whether a particular target exists in a collection and, if required, determining its position.

---

## Linear Search

Linear Search checks elements sequentially, one after another, until:

- The target is found, or
- All elements have been checked.

### Example

```python
numbers = [10, 20, 30, 40, 50]
target = 40

for num in numbers:
    if num == target:
        print("Found")
        break
```

---

## Why is it called Linear Search?

Elements are examined one by one in a linear/sequential order.

The amount of work can grow with the number of elements.

---

## Best Case

Target is the first element.

```text
[10, 20, 30, 40, 50]
 ↑
target
```

Only one comparison is required.

Time Complexity:

```text
O(1)
```

---

## Worst Case

Two situations can produce the worst case:

1. Target is the last element.
2. Target does not exist.

The algorithm may need to check every element.

Time Complexity:

```text
O(n)
```

---

## Important Observation

Linear Search does NOT require a sorted array.

Example:

```text
[40, 10, 70, 20, 5]
```

We can still search through it sequentially.

---

# Sorted Data Advantage

Consider:

```text
[10, 20, 30, 40, 50, 60, 70]
```

If the target is `60` and we check `40`:

```text
60 > 40
```

Because the array is sorted, everything to the left of `40` is also smaller than `60`.

Therefore:

```text
10, 20, 30, 40
```

can be eliminated from further consideration.

This idea leads to Binary Search.

---

# Pattern Recognition

Traversal

↓

Search Pattern

↓

Linear Search

---

# Key Takeaways

- Linear Search checks elements sequentially.
- It works on unsorted data.
- Best case: O(1)
- Worst case: O(n)
- Sorted data allows us to eliminate parts of the search space.
- Eliminating half the search space is the foundation of Binary Search.