# Day 28: Linked Lists — Deletion

## 1. What is Deletion?
Deletion is the process of removing a node from a linked list by updating the `next` reference or the `head` pointer.

Example: `10 → 20 → 30 → None`  
After deleting 20: `10 → 30 → None`

## 2. Delete at Beginning
```python
def delete_at_beginning(self):
    if self.head is None:
        print("List is empty")
        return

    self.head = self.head.next
```
- Move `head` to the second node.
- The previous first node is no longer reachable through the list.
- Works for a single-node list as well.
- **Time:** O(1) | **Space:** O(1)

## 3. Delete at End
```python
def delete_at_end(self):
    if self.head is None:
        print("List is empty")
        return

    if self.head.next is None:
        self.head = None
        return

    current = self.head
    while current.next.next is not None:
        current = current.next

    current.next = None
```
- Handle empty and single-node lists separately.
- Traverse until `current` reaches the second-last node.
- Set `current.next = None` to disconnect the last node.
- **Time:** O(n) | **Space:** O(1)

## 4. Delete at a Position
Positions are zero-based. To delete a node, move to the node immediately before it and bypass the target node.

```python
def delete_at_position(self, position):
    if position < 0 or self.head is None:
        print("Invalid position")
        return

    if position == 0:
        self.head = self.head.next
        return

    current = self.head

    for _ in range(position - 1):
        if current is None or current.next is None:
            print("Invalid position")
            return
        current = current.next

    if current.next is None:
        print("Invalid position")
        return

    current.next = current.next.next
```
- `position - 1` moves `current` to the previous node.
- `current.next = current.next.next` bypasses the node being deleted.
- Handles deletion at the beginning, end, and middle, including single-node lists.
- **Time:** O(n) | **Space:** O(1)

## 5. Important Edge Cases
- Empty list: deletion is invalid.
- Single-node list: deleting it makes `head = None`.
- Position 0: update `head`.
- Negative position: invalid.
- Position beyond the list length: invalid.
- Last valid index: deletes the last node.

## 6. Time Complexity

| Operation | Time | Auxiliary Space |
|---|---|---|
| Delete at beginning | O(1) | O(1) |
| Delete at end | O(n) | O(1) |
| Delete at position | O(n) | O(1) |

## 7. Key Takeaways
- `head = head.next` removes the first node from the list.
- `current.next = None` disconnects the last node.
- `current.next = current.next.next` bypasses a node.
- For middle or end deletion, locate the previous node first.
- A node is removed from the list by changing references, not necessarily by erasing its data.
