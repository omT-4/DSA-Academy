# Lesson 29: Linked List — Searching, Counting, Middle Node & Reversing

## 1. Introduction

A **Linked List** is a linear data structure consisting of nodes, where each node stores data and a reference to the next node.

Each node contains:
- `data`: The value stored in the node.
- `next`: A reference to the next node.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

- `head` points to the first node.
- `current` is a temporary reference used to traverse the list.
- `current.data` accesses the value stored in the current node.
- `current.next` refers to the next node.
- `current.next.data` accesses the next node's value.
- `current is None` means traversal has reached the end of the list.

Example:

```text
head
 |
 v
[5] -> [10] -> [15] -> [20] -> None
```

---

## 2. Searching in a Linked List

### Concept

Searching means finding whether a particular value exists in the linked list and, if it does, returning its position.

Unlike arrays, linked lists do not support direct index-based access. We must traverse nodes sequentially from the head.

### Algorithm

1. Set `current = head`.
2. Initialize `position = 0`.
3. Traverse while `current is not None`.
4. If `current.data == target`, return `position`.
5. Otherwise, move to the next node and increment `position`.
6. If the target is not found, return `-1`.

### Code

```python
def search(self, target):
    current = self.head
    position = 0

    while current is not None:
        if current.data == target:
            return position

        current = current.next
        position += 1

    return -1
```

### Dry Run

Linked list:

```text
5 -> 10 -> 15 -> 20 -> 25 -> None
```

Target: `20`

| Iteration | current.data | position | Comparison |
|---|---:|---:|---|
| 1 | 5 | 0 | Not found |
| 2 | 10 | 1 | Not found |
| 3 | 15 | 2 | Not found |
| 4 | 20 | 3 | Found |

Output:

```text
3
```

The function immediately returns `3` when the target is found, so it doesn't continue traversing the list.

### Edge Cases

- Empty list: returns `-1`.
- Target found at the head: returns `0`.
- Target found at the last node: returns its final zero-based position.
- Target not present: returns `-1`.
- Duplicate values: returns the position of the first occurrence.

### Complexity

- Best case: O(1), if the target is at the head.
- Average case: O(n).
- Worst case: O(n), if the target is at the end or absent.
- Auxiliary space: O(1).

---

## 3. Counting Nodes in a Linked List

### Concept

Counting nodes means finding the total number of nodes in the linked list.

We traverse the list and increase a counter for every node visited.

### Algorithm

1. Initialize `current = head`.
2. Initialize `count = 0`.
3. Traverse while `current is not None`.
4. Increment `count` by one for each node.
5. Move `current` to the next node.
6. Return `count` after traversal.

### Code

```python
def count_nodes(self):
    current = self.head
    count = 0

    while current is not None:
        count += 1
        current = current.next

    return count
```

### Dry Run

Linked list:

```text
5 -> 10 -> 15 -> 20 -> 25 -> None
```

| Iteration | current.data | count |
|---|---:|---:|
| Start | 5 | 0 |
| 1 | 5 | 1 |
| 2 | 10 | 2 |
| 3 | 15 | 3 |
| 4 | 20 | 4 |
| 5 | 25 | 5 |

Once `current` becomes `None`, the loop ends.

Output:

```text
5
```

### Edge Cases

- Empty list: returns `0`.
- Single-node list: returns `1`.
- Multiple nodes: returns the total number of nodes.

### Complexity

- Time: O(n), as every node is visited once.
- Auxiliary space: O(1), as only a counter and pointer are used.

---

## 4. Finding the Middle Node

### Concept

Finding the middle node can be done efficiently using the **Slow and Fast Pointer Technique**, also known as the Tortoise and Hare technique.

We use two pointers:
- `slow`: moves one node at a time.
- `fast`: moves two nodes at a time.

When `fast` reaches the end of the list, `slow` will be at the middle.

### Algorithm

1. Initialize `slow = head` and `fast = head`.
2. Continue while `fast is not None` and `fast.next is not None`.
3. Move `slow` one node forward.
4. Move `fast` two nodes forward.
5. When the loop ends, return `slow`.

### Code

```python
def find_middle(self):
    slow = self.head
    fast = self.head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow
```

### Dry Run — Odd Number of Nodes

Linked list:

```text
10 -> 20 -> 30 -> 40 -> 50 -> None
```

| Iteration | slow | fast |
|---|---:|---:|
| Start | 10 | 10 |
| 1 | 20 | 30 |
| 2 | 30 | 50 |

Now `fast.next` is `None`, so the loop stops.

The middle node is:

```text
30
```

### Dry Run — Even Number of Nodes

Linked list:

```text
10 -> 20 -> 30 -> 40 -> None
```

| Iteration | slow | fast |
|---|---:|---:|
| Start | 10 | 10 |
| 1 | 20 | 30 |
| 2 | 30 | None |

The middle node returned is `30`, which is the **second middle** of the list.

### Edge Cases

- Empty list: returns `None`.
- Single-node list: returns that node.
- Odd number of nodes: returns the exact middle.
- Even number of nodes: returns the second middle.

### Why Does It Work?

The `fast` pointer travels twice as quickly as the `slow` pointer. By the time `fast` reaches the end, `slow` has travelled approximately half the list.

This allows us to find the middle in one traversal without first counting all the nodes.

### Complexity

- Time: O(n).
- Auxiliary space: O(1).

---

## 5. Reversing a Linked List

### Concept

Reversing a linked list means changing the direction of every node's `next` reference so that the last node becomes the first.

Original list:

```text
5 -> 10 -> 15 -> 20 -> 25 -> None
```

Reversed list:

```text
25 -> 20 -> 15 -> 10 -> 5 -> None
```

We can reverse the list in place using three pointers:
- `prev`: points to the previous node.
- `current`: points to the node currently being processed.
- `next_node`: temporarily saves the next node before the link is changed.

### Algorithm

1. Initialize `prev = None`.
2. Initialize `current = head`.
3. While `current is not None`:
   - Save `current.next` in `next_node`.
   - Reverse the link by assigning `current.next = prev`.
   - Move `prev` to `current`.
   - Move `current` to `next_node`.
4. Update `head = prev`.

### Code

```python
def reverse(self):
    prev = None
    current = self.head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    self.head = prev
```

### Understanding the Pointers

- `current` is a reference to a node, not the node's data.
- `current.data` is the value stored in that node.
- `current.next` is a reference to the next node.
- `next_node` preserves the original next reference so we don't lose access to the remaining list.

**Important:** Save `current.next` before changing it. Otherwise, the remaining nodes could become unreachable from `current`.

### Dry Run

Original list:

```text
5 -> 10 -> 15 -> 20 -> 25 -> None
```

| Iteration | prev | current | next_node |
|---|---:|---:|---:|
| Start | None | 5 | — |
| 1 | 5 | 10 | 10 |
| 2 | 10 | 15 | 15 |
| 3 | 15 | 20 | 20 |
| 4 | 20 | 25 | 25 |
| 5 | 25 | None | None |

Each iteration reverses one link.

After the first iteration:

```text
None <- 5    10 -> 15 -> 20 -> 25 -> None
```

After the second iteration:

```text
None <- 5 <- 10    15 -> 20 -> 25 -> None
```

After the third iteration:

```text
None <- 5 <- 10 <- 15    20 -> 25 -> None
```

After the fourth iteration:

```text
None <- 5 <- 10 <- 15 <- 20    25 -> None
```

After the fifth iteration:

```text
None <- 5 <- 10 <- 15 <- 20 <- 25
```

At this point, `current` is `None`, so the loop ends. Finally, `head = prev` makes `25` the new head.

Final list:

```text
25 -> 20 -> 15 -> 10 -> 5 -> None
```

### Edge Cases

- Empty list: remains empty (`head` is `None`).
- Single-node list: remains unchanged.
- Multiple nodes: all links are reversed.
- The original list is modified in place; no new list is created.

### Complexity

- Time: O(n), as each node is visited once.
- Auxiliary space: O(1), as only three pointers are used.

---

## 6. Important Pointer Concepts

| Expression | Meaning |
|---|---|
| `current` | Reference to the current node |
| `current.data` | Value stored in the current node |
| `current.next` | Reference to the next node |
| `current.next.data` | Value stored in the next node |
| `current is None` | No current node; traversal has ended |
| `current.next is None` | Current node is the last node |
| `slow is fast` | Both references point to the same node |

**Remember:** Two variables can refer to the same node. Comparing them with `is` checks whether they reference the exact same object, rather than simply containing equal data.

---

## 7. Common Mistakes

1. **Forgetting to move `current`:** This can cause an infinite loop during traversal.
2. **Incrementing `position` incorrectly:** Start at zero and increment once after moving to the next node.
3. **Using `fast.next` without checking `fast`:** This can cause an error when `fast` is `None`. Always check `fast is not None` first.
4. **Losing the remaining list while reversing:** Always save `current.next` in `next_node` before changing the link.
5. **Forgetting to update `head`:** After reversing, assign `self.head = prev`.
6. **Confusing a node with its data:** `current` refers to a node; `current.data` is the value.
7. **Assuming an even-sized list has one exact middle:** This implementation returns the second middle.

---

## 8. Combined Complexity Summary

| Operation | Best Time | Worst Time | Auxiliary Space |
|---|---:|---:|---:|
| Search | O(1) | O(n) | O(1) |
| Count nodes | O(n) | O(n) | O(1) |
| Find middle | O(1) | O(n) | O(1) |
| Reverse | O(n) | O(n) | O(1) |

---

## 9. Practice Questions

### Question 1: Searching

Given:

```text
4 -> 8 -> 12 -> 16 -> 20 -> None
```

Find the zero-based position of `16`. What does the function return if the target is `100`?

**Solution:**
- `16` is at index `3`, so the function returns `3`.
- `100` is not present, so the function returns `-1`.

### Question 2: Counting Nodes

Given:

```text
7 -> 14 -> 21 -> 28 -> None
```

How many nodes are present?

**Solution:** `4`

### Question 3: Finding the Middle

Given:

```text
5 -> 10 -> 15 -> 20 -> 25 -> 30 -> 35 -> None
```

Where will `slow` be after two iterations?

**Solution:** `25`? No. Starting at `5`, `slow` moves to `10` after iteration 1 and `15` after iteration 2. Therefore, `slow` is at `15`.

After three iterations, `slow` reaches `20`, the middle node.

### Question 4: Even-Length Middle

Given:

```text
10 -> 20 -> 30 -> 40 -> None
```

Which node does `find_middle()` return?

**Solution:** `30`, the second middle node.

### Question 5: Reversing

Given:

```text
1 -> 2 -> 3 -> None
```

What is the final list after reversing?

**Solution:**

```text
3 -> 2 -> 1 -> None
```

---

## 10. Key Takeaways

- Linked lists require sequential traversal to access nodes.
- Searching returns the first matching zero-based index or `-1`.
- Counting nodes requires visiting each node once.
- Slow and fast pointers find the middle in a single traversal.
- The middle-finding method returns the second middle for even-sized lists.
- Reversing a linked list in place requires careful management of three pointers.
- All four operations use O(1) auxiliary space.
- Understanding references and pointer movement is essential for linked list problems.

**Lesson 29 Status: Completed**