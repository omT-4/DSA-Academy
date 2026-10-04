# Lesson 30: Linked List — Cycle Detection

## 1. Introduction

Cycle detection is the process of identifying whether a linked list contains a loop (cycle).

In a normal singly linked list, the last node points to `None`. However, in a cyclic linked list, the last node points to an earlier node, creating a loop.

**Normal Linked List:**
```text
10 -> 20 -> 30 -> 40 -> None
```

**Cyclic Linked List:**
```text
10 -> 20 -> 30 -> 40 -> 50
      ^                   |
      |___________________|
```

In a cyclic list, traversal may continue indefinitely because there is no `None` at the end.

## 2. Floyd's Cycle Detection Algorithm

Floyd's Cycle Detection Algorithm is also known as the **Tortoise and Hare Algorithm**.

It uses two pointers that move at different speeds:

- **Slow pointer (`slow`):** Moves one node at a time.
- **Fast pointer (`fast`):** Moves two nodes at a time.

### Working Principle

1. Initialize both pointers at the head.
2. Move `slow` one step forward.
3. Move `fast` two steps forward.
4. If both pointers refer to the same node, a cycle exists.
5. If `fast` or `fast.next` becomes `None`, the list has no cycle.

If a cycle exists, the fast pointer eventually catches up with the slow pointer inside the loop.

## 3. Python Implementation

```python
def has_cycle(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
```

### Code Explanation

| Code | Explanation |
|---|---|
| `slow = self.head` | Initialize slow pointer at the head |
| `fast = self.head` | Initialize fast pointer at the head |
| `while fast is not None and fast.next is not None` | Ensure fast can safely move two steps |
| `slow = slow.next` | Move slow one node forward |
| `fast = fast.next.next` | Move fast two nodes forward |
| `if slow is fast` | Check whether both point to the same node |
| `return True` | A cycle has been detected |
| `return False` | No cycle exists |

**Important:** Use `is` to check whether both pointers refer to the exact same node object, rather than simply having equal data.

## 4. Dry Run — Linked List Without a Cycle

Consider:

```text
5 -> 10 -> 15 -> 20 -> None
```

Initially:
- `slow = 5`
- `fast = 5`

| Iteration | Slow | Fast | Meet? |
|---|---:|---:|---|
| Start | 5 | 5 | — |
| 1 | 10 | 15 | No |
| 2 | 15 | None | No |

The loop terminates because `fast` becomes `None`.

**Output:**
```python
False
```

There is no cycle in this linked list.

## 5. Dry Run — Linked List With a Cycle

Consider:

```text
10 -> 20 -> 30 -> 40 -> 50
      ^                   |
      |___________________|
```

Node `50` points back to node `20`.

Initially:
- `slow = 10`
- `fast = 10`

| Iteration | Slow | Fast | Meet? |
|---|---:|---:|---|
| Start | 10 | 10 | — |
| 1 | 20 | 30 | No |
| 2 | 30 | 50 | No |
| 3 | 40 | 30 | No |
| 4 | 50 | 50 | Yes |

At iteration 4, both pointers reach the same node, `50`.

**Output:**
```python
True
```

A cycle is detected because both pointers refer to the same node.

## 6. Why Does Floyd's Algorithm Work?

When both pointers enter a cycle:
- The slow pointer moves one node per iteration.
- The fast pointer moves two nodes per iteration.
- Therefore, the fast pointer gains one node on the slow pointer each iteration within the cycle.

Since the cycle contains a finite number of nodes, the fast pointer will eventually catch up with the slow pointer.

If there is no cycle, the fast pointer will eventually reach `None`.

## 7. Edge Cases

| Case | Expected Result |
|---|---|
| Empty linked list | `False` |
| Single node pointing to `None` | `False` |
| Single node pointing to itself | `True` |
| Multiple nodes without a cycle | `False` |
| Multiple nodes with a cycle | `True` |
| Cycle begins at the head | `True` |
| Cycle begins at an intermediate node | `True` |

## 8. Complexity Analysis

**Time Complexity: O(n)**

The two pointers traverse the list at different speeds. The fast pointer either reaches the end or meets the slow pointer within a linear number of steps.

**Auxiliary Space: O(1)**

Only two pointers are used, regardless of the size of the linked list.

| Complexity | Value |
|---|---|
| Best-case time | O(1) |
| Worst-case time | O(n) |
| Auxiliary space | O(1) |

## 9. Common Mistakes

1. **Moving both pointers at the same speed:** This will not reliably detect a cycle.
2. **Forgetting the safety condition:** Always check `fast is not None` and `fast.next is not None` before moving two steps.
3. **Using `==` instead of `is`:** `is` explicitly checks whether both references point to the same node object.
4. **Returning `True` without a meeting:** A cycle is confirmed only when both pointers meet.
5. **Forgetting the final `return False`:** If the loop ends without a meeting, the list has no cycle.

## 10. Practice Questions

### Question 1
Given:
```text
5 -> 10 -> 15 -> 20 -> None
```
Where are `slow` and `fast` after the first iteration?

**Answer:**
- `slow = 10`
- `fast = 15`

### Question 2
Given:
```text
5 -> 10 -> 15 -> 20 -> 25 -> None
```
Where are both pointers after two iterations?

**Answer:**
- `slow = 15`
- `fast = 25`

### Question 3
Given:
```text
1 -> 2 -> 3 -> 4 -> 5
     ^              |
     |______________|
```
If node `5` points back to node `2`, what will `has_cycle()` return?

**Answer:** `True`

### Question 4
What happens if `fast` reaches `None` before both pointers meet?

**Answer:** The loop terminates and the function returns `False`.

### Question 5
What is the time and auxiliary space complexity of Floyd's Cycle Detection Algorithm?

**Answer:**
- Time: O(n)
- Auxiliary space: O(1)

## 11. Key Takeaways

- A cycle occurs when a node points back to an earlier node in the linked list.
- Floyd's algorithm uses slow and fast pointers.
- The slow pointer moves one step, while the fast pointer moves two steps.
- If both pointers meet at the same node, a cycle exists.
- If the fast pointer reaches `None`, there is no cycle.
- The algorithm works without using extra data structures such as sets or hash tables.
- Time complexity is O(n) and auxiliary space complexity is O(1).

**Lesson 30: Completed**
