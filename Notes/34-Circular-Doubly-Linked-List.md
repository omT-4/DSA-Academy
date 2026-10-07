# Circular Doubly Linked List

## 1. Core Idea

A Circular Doubly Linked List combines:

- Doubly Linked List → each node has `prev` and `next`
- Circular Linked List → last node connects back to first node

Main structure:

head ⇄ node ⇄ node ⇄ tail
 ↑                     ↓
 └─────────────────────┘

Important invariants:

tail.next == head
head.prev == tail

Unlike a normal doubly linked list:
- head.prev is NOT None
- tail.next is NOT None

---

## 2. Node Structure

Each node contains:

- data
- prev
- next

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

---

## 3. Head and Tail

The list maintains:

self.head
self.tail

For an empty list:

head = None
tail = None

For one node:

head == tail
head.next == head
head.prev == head

---

## 4. Circular Invariants

For a non-empty list:

tail.next == head
head.prev == tail

These connections must remain correct after every insertion and deletion.

---

## 5. Append

Add a node at the end.

Empty list:

head = new_node
tail = new_node
new_node.next = new_node
new_node.prev = new_node

Non-empty list:

new_node.prev = tail
new_node.next = head

tail.next = new_node
head.prev = new_node

tail = new_node

Time: O(1)

---

## 6. Prepend

Add a node at the beginning.

Empty list:

head = new_node
tail = new_node
new_node.next = new_node
new_node.prev = new_node

Non-empty list:

new_node.prev = tail
new_node.next = head

head.prev = new_node
tail.next = new_node

head = new_node

Time: O(1)

---

## 7. Forward Traversal

Start from head and follow next.

current = head

while True:
    process current
    current = current.next

    if current is head:
        break

Important:

Do NOT use:

while current is not None

because a circular list never reaches None.

---

## 8. Backward Traversal

Start from tail and follow prev.

current = tail

while True:
    process current
    current = current.prev

    if current is tail:
        break

---

## 9. Search

Search starts from head.

current = head

while True:
    if current.data == value:
        return True

    current = current.next

    if current is head:
        break

return False

Time: O(n)

---

## 10. Count

Start from head and keep moving through next.

if head is None:
    return 0

current = head
count = 0

while True:
    current = current.next
    count += 1

    if current is head:
        break

return count

Time: O(n)

---

## 11. Delete by Value

First search for the node.

current = head

while True:
    if current.data == value:
        break

    current = current.next

    if current is head:
        return False

---

## 12. Delete Only Node

If:

head == tail

then there is only one node.

Set:

head = None
tail = None

Return True.

---

## 13. Delete Head

If current is head:

head = head.next
tail.next = head
head.prev = tail

The next node becomes the new head.

---

## 14. Delete Tail

If current is tail:

tail = tail.prev
tail.next = head
head.prev = tail

The previous node becomes the new tail.

---

## 15. Delete Middle Node

For a middle node:

current.prev.next = current.next
current.next.prev = current.prev

This reconnects the two surrounding nodes.

Before:

A ⇄ B ⇄ C

Delete B:

A ⇄ C

---

## 16. Delete Complexity

Delete by value:

O(n)

because we may need to search for the node.

Once the node is already known:

O(1)

to remove it.

---

## 17. Complete Implementation

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        new_node.prev = self.tail
        new_node.next = self.head

        self.tail.next = new_node
        self.head.prev = new_node

        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        new_node.prev = self.tail
        new_node.next = self.head

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node

    def delete(self, value):
        if self.head is None:
            return False

        current = self.head

        while True:
            if current.data == value:
                break

            current = current.next

            if current is self.head:
                return False

        # Only node
        if self.head is self.tail:
            self.head = None
            self.tail = None
            return True

        # Delete head
        if current is self.head:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            return True

        # Delete tail
        elif current is self.tail:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
            return True

        # Delete middle
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
            return True

    def search(self, value):
        if self.head is None:
            return False

        current = self.head

        while True:
            if current.data == value:
                return True

            current = current.next

            if current is self.head:
                break

        return False

    def count(self):
        if self.head is None:
            return 0

        current = self.head
        count = 0

        while True:
            current = current.next
            count += 1

            if current is self.head:
                break

        return count

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end="->")
            current = current.next

            if current is self.head:
                break

        print("(back to head)")

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.tail

        while True:
            print(current.data, end="->")
            current = current.prev

            if current is self.tail:
                break

        print("(back to tail)")


---

## 18. Complexity Summary

| Operation | Time |
|---|---:|
| Append | O(1) |
| Prepend | O(1) |
| Search | O(n) |
| Count | O(n) |
| Display Forward | O(n) |
| Display Backward | O(n) |
| Delete by Value | O(n) |
| Delete Known Node | O(1) |

Auxiliary Space: O(1)

---

## 19. Important Rules

1. tail.next must always point to head.
2. head.prev must always point to tail.
3. Traversal cannot use None as the stopping condition.
4. Use `current is head` for forward traversal.
5. Use `current is tail` for backward traversal.
6. A one-node list points to itself in both directions.
7. Delete operations must update both next and prev pointers.
8. Append and prepend are O(1) when head and tail are maintained.

---

## 20. Common Mistakes

### Mistake 1
Using:

while current is not None

Wrong because the list is circular.

### Mistake 2
Forgetting:

tail.next = head

This breaks circularity.

### Mistake 3
Forgetting:

head.prev = tail

This breaks backward circularity.

### Mistake 4
Updating only one pointer during deletion.

Both sides must be updated.

### Mistake 5
Forgetting the one-node case.

When:

head == tail

deleting the node must make both None.

---

## 21. Interview Tips

Q: What makes a doubly linked list circular?

A:
The tail points to the head and the head points back to the tail.

tail.next == head
head.prev == tail

Q: Why is append O(1)?

A:
Because we maintain a tail pointer.

Q: Why can traversal not stop at None?

A:
Because circular lists do not contain a None link at the end.

Q: What is the advantage over a circular singly linked list?

A:
We can traverse in both directions because every node has a prev pointer.

---

## 22. Concept Connection

Singly Linked List:
next

Doubly Linked List:
prev + next

Circular Singly Linked List:
next + tail.next → head

Circular Doubly Linked List:
prev + next
tail.next → head
head.prev → tail

Circular Doubly Linked List provides:

- Forward traversal
- Backward traversal
- O(1) append with tail
- O(1) prepend with head
- O(1) deletion when the node is already known

---

## 23. Edge Cases

Always test:

1. Empty list
2. One node
3. Two nodes
4. Multiple nodes
5. Delete head
6. Delete tail
7. Delete middle
8. Delete only node
9. Search existing value
10. Search missing value
11. Count empty list
12. Count one node

---

## 24. Key Takeaways

Circular Doubly Linked List = Doubly Linked List + Circular Connections.

Most important invariant:

tail.next == head
head.prev == tail

The biggest difference from a normal doubly linked list is that traversal never reaches None.

Always maintain BOTH directions correctly.