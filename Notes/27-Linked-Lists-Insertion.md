# Lesson 27: Linked Lists — Insertion

## 1. Introduction

Insertion in a linked list means adding a new node at a specific position. Unlike arrays, linked lists do not require shifting elements. We update node references (`next`) to connect the new node.

## 2. Insert at Beginning

To insert a node at the beginning:
1. Create a new node.
2. Point its `next` to the current head.
3. Update `head` to the new node.

```python
new_node = Node(data)
new_node.next = self.head
self.head = new_node
```

This also works for an empty linked list, where `self.head` is `None`.

**Time Complexity:** O(1)  
**Auxiliary Space:** O(1)

## 3. Insert at End

To insert at the end without a tail pointer:
1. Create a new node.
2. If the list is empty, make it the head.
3. Otherwise, traverse to the last node.
4. Connect the last node to the new node.

```python
def append(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        return

    current = self.head

    while current.next is not None:
        current = current.next

    current.next = new_node
```

**Time Complexity:** O(n), because traversal may be required.  
**Auxiliary Space:** O(1)

## 4. Insert at a Specific Position

Positions are zero-based.

For `10 → 20 → 40 → None`, inserting `30` at position `2` produces:

`10 → 20 → 30 → 40 → None`

The `current` pointer should stop at the node just before the insertion position.

```python
new_node.next = current.next
current.next = new_node
```

The order is important: first connect the new node to the existing next node, then connect `current` to the new node. Reversing the order can lose the remaining chain.

## 5. Complete Insert-at-Position Method

```python
def insert_at_position(self, data, position):
    if position < 0:
        print("Invalid position")
        return

    new_node = Node(data)

    if position == 0:
        new_node.next = self.head
        self.head = new_node
        return

    current = self.head

    for _ in range(position - 1):
        if current is None:
            print("Invalid position")
            return
        current = current.next

    if current is None:
        print("Invalid position")
        return

    new_node.next = current.next
    current.next = new_node
```

This method:
- Allows insertion at position `0`, including when the list is empty.
- Allows insertion at the end, at position `n` for a list of `n` nodes.
- Rejects negative positions and positions beyond the end.

## 6. Understanding `head` and `current`

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

- `self.head` is an instance attribute that stores a reference to the first node.
- `current = self.head` creates a local reference to the same first node.
- `current` can move through the list without changing `self.head`.
- `self.head` remains the starting reference unless explicitly updated.

## 7. Insert at End With a Tail Pointer

A `tail` pointer stores a reference to the last node. It avoids traversing the list to append.

```python
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
```

When the list is empty, both `head` and `tail` point to the first node. For later insertions, connect the old tail to the new node and update `tail`.

**Time Complexity:** O(1)  
**Auxiliary Space:** O(1)

## 8. Time and Space Complexity

| Operation | Time Complexity | Auxiliary Space |
|---|---:|---:|
| Insert at beginning | O(1) | O(1) |
| Insert at end without tail | O(n) | O(1) |
| Insert at end with tail | O(1) | O(1) |
| Insert at a specific position | O(n) worst case | O(1) |

The new node requires O(1) additional storage; auxiliary space excludes that node.

## 9. Important Edge Cases

- Empty list, insert at position `0`.
- Non-empty list, insert at position `0`.
- Insert at position `n` to append.
- Negative position.
- Position greater than `n`.
- Single-node linked list.

## 10. Key Takeaways

- `head` points to the first node.
- `tail` points to the last node when maintained.
- Insertion changes links; it does not shift nodes.
- Insert at beginning takes O(1).
- Insert at end takes O(n) without a tail, or O(1) with a tail.
- Inserting at a position takes O(n) in the worst case.
- Assignment order matters when updating references.
