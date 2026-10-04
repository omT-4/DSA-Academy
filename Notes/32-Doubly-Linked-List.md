# Lesson 32: Doubly Linked List

## 1. Introduction

A Doubly Linked List (DLL) is a linear data structure in which each node contains data and two pointers: `prev` and `next`.

- `data`: Stores the value.
- `prev`: Points to the previous node.
- `next`: Points to the next node.

Unlike a Singly Linked List, a Doubly Linked List supports traversal in both directions.

**Structure:**

```text
None ← 10 ⇄ 20 ⇄ 30 → None
        head        tail
```

- The first node is the `head`, and its `prev` is `None`.
- The last node is the `tail`, and its `next` is `None`.

## 2. Node Implementation

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
```

Each node stores its value and two references. Both references are initially `None`.

## 3. Doubly Linked List Class

```python
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
```

- `head` points to the first node.
- `tail` points to the last node.
- Both are `None` when the list is empty.

Maintaining a tail pointer makes insertion at the end efficient.

## 4. Insertion at the End

```python
def append(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        self.tail = new_node
        return

    self.tail.next = new_node
    new_node.prev = self.tail
    self.tail = new_node
```

**Explanation:**

1. Create a new node.
2. If the list is empty, make the new node both `head` and `tail`.
3. Otherwise, link the current tail's `next` to the new node.
4. Set the new node's `prev` to the old tail.
5. Update `tail` to the new node.

**Dry run:**

Insert `10`, `20`, and `30`.

```text
Insert 10: 10
Insert 20: 10 ⇄ 20
Insert 30: 10 ⇄ 20 ⇄ 30
```

Time complexity: `O(1)` with a tail pointer.

## 5. Insertion at the Beginning

```python
def prepend(self, data):
    new_node = Node(data)

    if self.head is None:
        self.head = new_node
        self.tail = new_node
        return

    new_node.next = self.head
    self.head.prev = new_node
    self.head = new_node
```

**Explanation:**

1. Create a new node.
2. If the list is empty, set both `head` and `tail` to it.
3. Connect the new node's `next` to the current head.
4. Connect the old head's `prev` to the new node.
5. Update `head`.

**Dry run:**

```text
Before: 10 ⇄ 20 ⇄ 30
Insert: 5

After:  5 ⇄ 10 ⇄ 20 ⇄ 30
```

Time complexity: `O(1)`.

## 6. Traversal

### Forward Traversal

```python
def display_forward(self):
    current = self.head

    while current is not None:
        print(current.data, end=" <-> ")
        current = current.next

    print("None")
```

Start at `head` and follow `next` until reaching `None`.

### Backward Traversal

```python
def display_backward(self):
    current = self.tail

    while current is not None:
        print(current.data, end=" <-> ")
        current = current.prev

    print("None")
```

Start at `tail` and follow `prev` until reaching `None`.

For `10 ⇄ 20 ⇄ 30`:

```text
Forward:  10 <-> 20 <-> 30 <-> None
Backward: 30 <-> 20 <-> 10 <-> None
```

Time complexity for each traversal: `O(n)`.

## 7. Insertion at a Specific Position

The following method inserts a node at a zero-based index.

```python
def insert_at(self, index, data):
    if index < 0:
        raise IndexError("Invalid index")

    if index == 0:
        self.prepend(data)
        return

    current = self.head
    position = 0

    while current is not None and position < index:
        current = current.next
        position += 1

    if current is None:
        if position == index:
            self.append(data)
            return
        raise IndexError("Index out of range")

    new_node = Node(data)
    new_node.prev = current.prev
    new_node.next = current

    current.prev.next = new_node
    current.prev = new_node
```

**Dry run:**

Insert `15` at index `1` in `10 ⇄ 20 ⇄ 30`.

```text
Before: 10 ⇄ 20 ⇄ 30
After:  10 ⇄ 15 ⇄ 20 ⇄ 30
```

Pointer updates:

- `new_node.prev = current.prev`
- `new_node.next = current`
- `current.prev.next = new_node`
- `current.prev = new_node`

The links must be updated in both directions.

Time complexity: `O(n)` due to searching for the position.

## 8. Deletion by Value

```python
def delete(self, value):
    current = self.head

    while current is not None and current.data != value:
        current = current.next

    if current is None:
        return False

    if current.prev is not None:
        current.prev.next = current.next
    else:
        self.head = current.next

    if current.next is not None:
        current.next.prev = current.prev
    else:
        self.tail = current.prev

    return True
```

**Explanation:**

1. Search for the node containing the target value.
2. If the node is not found, return `False`.
3. If it has a previous node, connect that node's `next` to the deleted node's `next`; otherwise, update `head`.
4. If it has a next node, connect that node's `prev` to the deleted node's `prev`; otherwise, update `tail`.
5. Return `True`.

**Dry run: Delete node 20**

```text
Before: 10 ⇄ 20 ⇄ 30
After:  10 ⇄ 30
```

The node before `20` now points forward to `30`, and node `30` points backward to `10`.

Time complexity: `O(n)` for searching. If a node reference is already known, unlinking it takes `O(1)`.

## 9. Edge Cases

| Case | Expected behaviour |
|---|---|
| Empty list | `head` and `tail` are `None` |
| Insert into empty list | New node becomes both `head` and `tail` |
| Delete from empty list | No change |
| Delete the only node | Both `head` and `tail` become `None` |
| Delete head | New head's `prev` becomes `None` |
| Delete tail | New tail's `next` becomes `None` |
| Delete missing value | List remains unchanged |
| Insert at index 0 | Equivalent to prepend |
| Insert at list length | Equivalent to append |

## 10. Complete Time Complexity

| Operation | Time |
|---|---:|
| Insert at beginning | `O(1)` |
| Insert at end | `O(1)` |
| Forward traversal | `O(n)` |
| Backward traversal | `O(n)` |
| Search by value | `O(n)` |
| Insert at index | `O(n)` |
| Delete by value | `O(n)` |
| Unlink a known node | `O(1)` |

Auxiliary space for pointer-based operations: `O(1)`. The linked list itself requires `O(n)` space for its nodes.

## 11. Common Mistakes

1. Forgetting to update both `prev` and `next`.
2. Forgetting to update `head` or `tail` after insertion or deletion at an endpoint.
3. Not handling the empty-list case.
4. Failing to set the new head's `prev` to `None`.
5. Failing to set the new tail's `next` to `None`.
6. Confusing moving a temporary pointer with updating a node's actual link.

## 12. Practice Questions

**Q1. What are the two pointers in a DLL?**  
`prev` and `next`.

**Q2. Why is a DLL traversable backward?**  
Each node stores a reference to its previous node.

**Q3. What happens when a node is inserted into an empty list?**  
Both `head` and `tail` point to the new node.

**Q4. What should happen to the new head's `prev` after deleting the old head?**  
It must be set to `None`.

**Q5. What should happen when the only node is deleted?**  
Both `head` and `tail` become `None`.

**Q6. What is the time complexity of appending when a tail pointer is maintained?**  
`O(1)`.

**Q7. What is the time complexity of deleting by value?**  
`O(n)` because the target node must be searched for.

## 13. LeetCode Practice

- [LeetCode 707: Design Linked List](https://leetcode.com/problems/design-linked-list/) — Medium
- [LeetCode 146: LRU Cache](https://leetcode.com/problems/lru-cache/) — Medium

These problems help practise node references, insertion, deletion, and combining a doubly linked list with other data structures.

## 14. Key Takeaways

- A DLL uses `prev` and `next` pointers.
- It supports forward and backward traversal.
- Maintaining `head` and `tail` enables `O(1)` insertion at both ends.
- Insertion and deletion require careful updates to both neighbouring links.
- Always handle empty-list and single-node cases.
- Searching by value takes `O(n)` time, while unlinking a known node takes `O(1)` time.
