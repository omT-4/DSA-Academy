# Lesson 31: Finding the Starting Node of a Cycle in a Linked List

## 1. Introduction

In a linked list, a cycle occurs when a node points back to a previous node instead of pointing to `None`. This creates a loop, causing us to traverse the same nodes repeatedly.

In Lesson 30, we learned how to detect whether a cycle exists using **Floyd's Tortoise and Hare Algorithm**.

In this lesson, we will learn how to find the **exact node where the cycle begins**.

**Example:**

```text
10 → 20 → 30 → 40 → 50 → 60
          ↑              |
          └──────────────┘
```

Here, node `60` points back to node `30`.

- Cycle exists: Yes
- Cycle starting node: `30`
- Cycle length: `4`

## 2. Floyd's Cycle Detection Algorithm

We use two pointers:

- **Slow pointer:** Moves one node at a time.
- **Fast pointer:** Moves two nodes at a time.

If a cycle exists, both pointers will eventually meet inside the cycle.

However, **the meeting point is not necessarily the starting node of the cycle**.

To find the starting node, we use a two-phase approach.

## 3. Two-Phase Algorithm

### Phase 1: Detect the cycle

1. Initialize both `slow` and `fast` at the head.
2. Move `slow` one step and `fast` two steps.
3. If they meet, a cycle exists.
4. If `fast` or `fast.next` becomes `None`, no cycle exists.

### Phase 2: Find the cycle's starting node

1. Reset `slow` to the head of the linked list.
2. Keep `fast` at the meeting point from Phase 1.
3. Move both pointers one step at a time.
4. The node where they meet again is the starting node of the cycle.

## 4. Python Implementation

```python
def detect_cycle_start(self):
    slow = self.head
    fast = self.head

    # Phase 1: Detect cycle
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            break
    else:
        return None

    # Phase 2: Find cycle starting node
    slow = self.head

    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow
```

## 5. Code Explanation

**Phase 1:**

```python
slow = self.head
fast = self.head
```

Both pointers begin at the head.

```python
while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next
```

The loop checks that the fast pointer can safely move two steps. The slow pointer moves one step while the fast pointer moves two.

```python
if slow is fast:
    break
```

We compare node identity, not just the values stored in the nodes. If both pointers refer to the same node object, a cycle has been detected.

```python
else:
    return None
```

The `else` belongs to the `while` loop. It executes if the loop finishes normally, without hitting `break`. This means no cycle was detected, so we return `None`.

**Phase 2:**

```python
slow = self.head
```

Reset the slow pointer to the beginning of the linked list.

```python
while slow is not fast:
    slow = slow.next
    fast = fast.next
```

Move both pointers one step at a time. They will meet at the cycle's starting node.

```python
return slow
```

Return the node object where both pointers meet.

## 6. Dry Run 1: Finding the Cycle Start

**Linked List:**

```text
10 → 20 → 30 → 40 → 50 → 60
          ↑              |
          └──────────────┘
```

Node `60` points back to node `30`.

### Phase 1: Detect the cycle

| Iteration | Slow | Fast |
|---|---:|---:|
| Start | 10 | 10 |
| 1 | 20 | 30 |
| 2 | 30 | 50 |
| 3 | 40 | 30 |
| 4 | 50 | 50 |

Both pointers meet at node `50`.

This confirms that a cycle exists, but node `50` is not the cycle's starting node.

### Phase 2: Find the cycle start

Reset `slow` to node `10`. Keep `fast` at node `50`.

| Step | Slow | Fast |
|---|---:|---:|
| Start | 10 | 50 |
| 1 | 20 | 60 |
| 2 | 30 | 30 |

Both pointers meet at node `30`.

**Result: Node `30` is the starting node of the cycle.**

## 7. Dry Run 2: Linked List Without a Cycle

```text
5 → 10 → 15 → 20 → None
```

| Iteration | Slow | Fast |
|---|---:|---:|
| Start | 5 | 5 |
| 1 | 10 | 15 |
| 2 | 15 | None |

The fast pointer reaches `None`, so the loop ends without finding a meeting point.

**Result: `None` (no cycle exists).**

Phase 2 is never executed.

## 8. Why Does Phase 2 Work?

Suppose:

- `L` = distance from the head to the cycle start
- `C` = length of the cycle
- `x` = distance from the cycle start to the meeting point

When slow and fast meet in Phase 1, the fast pointer has travelled twice as far as the slow pointer.

The difference in their travelled distances is a whole number of cycle lengths. This gives:

```text
L + x = kC
```

for some positive integer `k`.

Rearranging:

```text
L = kC - x
```

This means the distance from the meeting point to the cycle start, moving forward around the cycle, is equal to the distance from the head to the cycle start, allowing for one or more full laps around the cycle.

Therefore, resetting one pointer to the head and moving both pointers one step at a time makes them meet at the cycle start.

## 9. Edge Cases

| Case | Input | Expected Result |
|---|---|---|
| Empty list | `head = None` | `None` |
| Single node, no cycle | `10 → None` | `None` |
| Single node, self-cycle | `10 → 10` | Node `10` |
| Cycle starts at head | `10 → 20 → 30 → 10` | Node `10` |
| Cycle starts in middle | `10 → 20 → 30 → 40 → 30` | Node `30` |
| Cycle starts at last node | `10 → 20 → 30 → 20` | Node `20` |

## 10. Time and Space Complexity

**Time Complexity: `O(n)`**

- Phase 1 traverses the list until the pointers meet or the fast pointer reaches the end.
- Phase 2 traverses toward the cycle start.
- Both phases take linear time overall.

**Auxiliary Space Complexity: `O(1)`**

Only two pointers are used, regardless of the size of the linked list.

## 11. Common Mistakes

1. **Returning the Phase 1 meeting point:** The first meeting point is inside the cycle, not necessarily at its start.
2. **Forgetting to reset `slow`:** Phase 2 requires resetting `slow` to the head.
3. **Moving `fast` two steps in Phase 2:** Both pointers must move exactly one step in Phase 2.
4. **Comparing node values instead of node identity:** Use `is` to compare whether both pointers refer to the same node.
5. **Not handling the no-cycle case:** Return `None` if Phase 1 finishes without a meeting.

## 12. Practice Questions

### Q1. What is the purpose of Phase 1?

**Answer:** To detect whether a cycle exists and find a meeting point inside it.

### Q2. Is the Phase 1 meeting point always the cycle's starting node?

**Answer:** No. It can be any node within the cycle.

### Q3. What happens to `slow` at the beginning of Phase 2?

**Answer:** It is reset to the head, while `fast` remains at the Phase 1 meeting point.

### Q4. How far does each pointer move in Phase 2?

**Answer:** Both pointers move one node at a time.

### Q5. What does the algorithm return if there is no cycle?

**Answer:** `None`.

### Q6. What is the auxiliary space complexity?

**Answer:** `O(1)` because only two pointers are used.

## 13. Key Takeaways

- Floyd's algorithm can both detect a cycle and locate its starting node.
- Phase 1 detects the cycle and identifies a meeting point.
- Phase 2 resets `slow` to the head and moves both pointers one step at a time.
- Their second meeting identifies the cycle's starting node.
- The algorithm takes `O(n)` time and `O(1)` auxiliary space.

## 14. LeetCode Practice

**LeetCode 142: Linked List Cycle II**

Problem: Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return `None`.

The expected solution uses Floyd's Tortoise and Hare Algorithm.

Link: https://leetcode.com/problems/linked-list-cycle-ii/

## 15. Revision Checklist

- [ ] Understand how Floyd's cycle detection works.
- [ ] Know why the Phase 1 meeting point may differ from the cycle start.
- [ ] Understand why `slow` is reset to the head.
- [ ] Be able to dry run both phases.
- [ ] Handle empty lists and lists without cycles.
- [ ] Know the time and auxiliary space complexity.
- [ ] Attempt LeetCode 142 independently.
