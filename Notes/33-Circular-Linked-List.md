# Lesson 33 — Circular Linked List

## 1. Core Idea

A Circular Linked List is a linked list where the last node does NOT point to `None`.

Instead:

`tail.next == head`

Example:

10 → 20 → 30
↑         ↓
└─────────┘

So the list forms a circle.

### Key Difference

Singly Linked List:
`10 → 20 → 30 → None`

Circular Linked List:
`10 → 20 → 30 → 10 → 20 → ...`

The most important invariant is:

`tail.next == head`

---

## 2. Node Structure

A circular singly linked list uses the same node structure as a normal singly linked list.

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

Each node contains:

- `data` → stores the value
- `next` → points to the next node

---

## 3. Head and Tail

We maintain:

    self.head
    self.tail

Example:

    10 → 20 → 30
    ↑         ↓
    └─────────┘

Here:

`head = 10`

`tail = 30`

And:

`tail.next = head`

So:

`30.next = 10`

---

## 4. Empty List

Initially:

    self.head = None
    self.tail = None

There are no nodes.

---

## 5. Single Node

When there is only one node:

    10
    ↑↓
    └┘

Both `head` and `tail` point to the same node.

And:

`head == tail`

Also:

`head.next == head`

Because the node points back to itself.

---

# 6. Append

Append means adding a node at the end.

Example:

Before:

`10 → 20 → 10`

Add `30`.

After:

`10 → 20 → 30 → 10`

The important updates are:

1. New node points to head.
2. Old tail points to new node.
3. New node becomes tail.

Code:

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.tail = new_node

### Complexity

Time: `O(1)`

Space: `O(1)` auxiliary space.

---

# 7. Prepend

Prepend means adding a node at the beginning.

Before:

`10 → 20 → 30 → 10`

Add `5`.

After:

`5 → 10 → 20 → 30 → 5`

Important updates:

1. New node points to old head.
2. Tail points to new head.
3. New node becomes head.

Code:

    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            return

        new_node.next = self.head
        self.tail.next = new_node
        self.head = new_node

### Complexity

Time: `O(1)`

Space: `O(1)` auxiliary space.

---

# 8. Traversal

Normal linked lists use:

`while current is not None`

But that DOES NOT work for a circular linked list because `current` never becomes `None`.

Instead, we stop when we return to the head.

Code:

    def display(self):
        if self.head is None:
            print("List is empty")
            return

        current = self.head

        while True:
            print(current.data, end=" -> ")
            current = current.next

            if current is self.head:
                break

        print("(back to head)")

Example output:

`10 -> 20 -> 30 -> (back to head)`

### Important Rule

Circular traversal stops when:

`current is head`

---

# 9. Why Use `is`?

We use:

    if current is self.head:

instead of:

    if current.data == self.head.data:

Because we want to know whether we have returned to the SAME NODE.

Two different nodes can contain the same value.

Example:

`10 → 20 → 10`

The second `10` may be a different node.

Therefore node identity is safer.

---

# 10. Search

Search checks whether a value exists.

Code:

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

### Complexity

Time: `O(n)`

Space: `O(1)` auxiliary space.

---

# 11. Count Nodes

We cannot use:

`while current is not None`

because a circular list never reaches `None`.

Instead, stop when we return to head.

Code:

    def count(self):
        if self.head is None:
            return 0

        count = 0
        current = self.head

        while True:
            count += 1
            current = current.next

            if current is self.head:
                break

        return count

### Complexity

Time: `O(n)`

Space: `O(1)` auxiliary space.

---

# 12. Delete a Node by Value

Deletion is slightly more complicated because we need both:

- `current`
- `previous`

Example:

`10 → 20 → 30 → 10`

Suppose we want to delete `20`.

We need:

`previous = 10`

`current = 20`

Then:

`previous.next = current.next`

Result:

`10 → 30 → 10`

---

# 13. Why Is `previous = tail` Initially?

This is one of the most important ideas.

In a normal singly linked list:

`head → ... → None`

There is no node before head.

But in a circular list:

`tail → head`

Therefore, the node before head is the tail.

So we initialize:

    previous = self.tail

Then:

    current = self.head

This allows us to correctly delete the head.

---

# 14. Delete Implementation

Code:

    def delete(self, value):
        if self.head is None:
            return False

        current = self.head
        previous = self.tail

        while True:
            if current.data == value:
                break

            previous = current
            current = current.next

            if current is self.head:
                return False

        # Only node
        if current is self.head and current is self.tail:
            self.head = None
            self.tail = None
            return True

        # Delete head
        if current is self.head:
            self.head = current.next
            self.tail.next = self.head
            return True

        # Delete middle or tail
        previous.next = current.next

        # Delete tail
        if current is self.tail:
            self.tail = previous

        return True

---

# 15. Delete Only Node

Example:

`10 → 10`

Here:

`head == tail`

If we delete `10`:

    self.head = None
    self.tail = None

The list becomes empty.

---

# 16. Delete Head

Example:

Before:

`10 → 20 → 30 → 10`

Delete `10`.

New head:

`20`

So:

    self.head = current.next

But we must also maintain the circular connection:

    self.tail.next = self.head

Result:

`20 → 30 → 20`

---

# 17. Delete Middle Node

Example:

`10 → 20 → 30 → 10`

Delete `20`.

We have:

`previous = 10`

`current = 20`

Then:

    previous.next = current.next

So:

`10 → 30 → 10`

---

# 18. Delete Tail

Example:

`10 → 20 → 30 → 10`

Delete `30`.

Here:

`previous = 20`

`current = 30`

First:

    previous.next = current.next

Since `current.next` is head:

`20.next = 10`

Then:

    self.tail = previous

So:

`10 → 20 → 10`

### Important

We do NOT need:

    self.tail.next = self.head

again.

Why?

Because:

    previous.next = current.next

already made:

`new_tail.next = head`

---

# 19. Why Is Delete Tail O(n)?

A common mistake is thinking:

"Since we have a tail pointer, deleting the tail must be O(1)."

That is NOT true for a circular singly linked list.

The tail pointer tells us:

`tail = 30`

But it does NOT tell us:

`previous = 20`

We still have to traverse the list to find the node before tail.

Therefore:

Delete tail by value → `O(n)`

If we already had a reference to the previous node, the pointer update itself would be `O(1)`.

A doubly linked list solves this problem because every node has a `prev` pointer.

---

# 20. Complete Circular Linked List

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None


    class CircularLinkedList:
        def __init__(self):
            self.head = None
            self.tail = None


        def append(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                return

            new_node.next = self.head
            self.tail.next = new_node
            self.tail = new_node


        def prepend(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
                return

            new_node.next = self.head
            self.tail.next = new_node
            self.head = new_node


        def display(self):
            if self.head is None:
                print("List is empty")
                return

            current = self.head

            while True:
                print(current.data, end=" -> ")
                current = current.next

                if current is self.head:
                    break

            print("(back to head)")


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

            count = 0
            current = self.head

            while True:
                count += 1
                current = current.next

                if current is self.head:
                    break

            return count


        def delete(self, value):
            if self.head is None:
                return False

            current = self.head
            previous = self.tail

            while True:
                if current.data == value:
                    break

                previous = current
                current = current.next

                if current is self.head:
                    return False

            # Only node
            if current is self.head and current is self.tail:
                self.head = None
                self.tail = None
                return True

            # Delete head
            if current is self.head:
                self.head = current.next
                self.tail.next = self.head
                return True

            # Delete middle or tail
            previous.next = current.next

            # Delete tail
            if current is self.tail:
                self.tail = previous

            return True

---

# 21. Example Usage

    cll = CircularLinkedList()

    cll.append(10)
    cll.append(20)
    cll.append(30)

    cll.display()

    cll.prepend(5)

    cll.display()

    print(cll.search(20))
    print(cll.search(50))

    print(cll.count())

    cll.delete(5)
    cll.display()

    cll.delete(20)
    cll.display()

    cll.delete(30)
    cll.display()

Expected output:

    10 -> 20 -> 30 -> (back to head)

    5 -> 10 -> 20 -> 30 -> (back to head)

    True
    False

    4

    10 -> 20 -> 30 -> (back to head)

    10 -> 30 -> (back to head)

    10 -> (back to head)

---

# 22. Complexity Summary

| Operation | Time |
|---|---:|
| Append | O(1) |
| Prepend | O(1) |
| Display | O(n) |
| Search | O(n) |
| Count | O(n) |
| Delete by value | O(n) |
| Delete head | O(1) once node is known |
| Delete tail by value | O(n) |

Auxiliary space for these operations: `O(1)`.

---

# 23. Edge Cases

Always consider:

1. Empty list
2. One-node list
3. Two-node list
4. Delete head
5. Delete middle
6. Delete tail
7. Delete only node
8. Search in empty list
9. Search for missing value
10. Duplicate values

---

# 24. Common Mistakes

### Mistake 1: Using `while current is not None`

Wrong for circular linked lists.

Why?

Because `current` never becomes `None`.

Use:

    while True:
        ...
        if current is self.head:
            break


### Mistake 2: Forgetting `tail.next = head`

The circular invariant must always be maintained:

`tail.next == head`


### Mistake 3: Forgetting the one-node case

For one node:

`head == tail`

and:

`head.next == head`


### Mistake 4: Forgetting to update tail when deleting the tail

If the old tail is deleted:

    self.tail = previous


### Mistake 5: Thinking tail deletion is O(1)

A tail pointer does not give us the previous node in a singly linked list.

Therefore finding the previous node requires traversal.

---

# 25. Important Rules

Remember these rules:

1. Circular list does not end with `None`.
2. `tail.next == head`.
3. Traversal stops when we return to head.
4. One-node list has `head == tail`.
5. One-node list has `head.next == head`.
6. For deletion, initialize `previous = tail`.
7. Deleting head requires updating `tail.next`.
8. Deleting tail requires finding the previous node.
9. Tail deletion in circular singly linked list is `O(n)`.
10. Node identity can be checked using `is`.

---

# 26. Interview Tips

### Q: What is a circular linked list?

A linked list where the last node points back to the first node instead of `None`.

### Q: What is the key invariant?

`tail.next == head`

### Q: How do you know traversal is complete?

Stop when the current node becomes the head again.

### Q: Why can't we use `current != None`?

Because a circular linked list never reaches `None`.

### Q: Why is tail deletion O(n)?

Because we need to find the node before tail, and a singly linked list does not store previous pointers.

### Q: What is the advantage of a circular linked list?

It is useful when data needs to be processed repeatedly in a cycle.

Examples:

- Round-robin scheduling
- Multiplayer turn systems
- Circular buffers
- Repeating playlists
- CPU scheduling concepts

---

# 27. Concept Connection

### Singly Linked List

    head → 10 → 20 → 30 → None

Each node only knows the next node.

### Doubly Linked List

    None ← 10 ⇄ 20 ⇄ 30 → None

Each node knows:

- previous node
- next node

### Circular Singly Linked List

    10 → 20 → 30
    ↑         ↓
    └─────────┘

Each node knows the next node, and the last node connects back to head.

### Circular Doubly Linked List

Combines both ideas:

- `next`
- `prev`
- last node connects to first
- first node connects back to last

---

# 28. Practice Problems

Recommended practice:

1. Implement Circular Linked List from scratch.
2. Implement append.
3. Implement prepend.
4. Implement traversal.
5. Implement search.
6. Implement count.
7. Implement delete by value.
8. Handle deletion of head.
9. Handle deletion of tail.
10. Handle deletion of the only node.

LeetCode-style practice:

- Design Linked List
- Linked List Cycle
- Linked List Cycle II

---

# 29. Key Takeaways

The most important things to remember:

`tail.next == head`

`head == tail` for one node.

Traversal:

    while True:
        ...
        if current is head:
            break

Deletion starts with:

    current = head
    previous = tail

Delete middle:

    previous.next = current.next

Delete head:

    head = current.next
    tail.next = head

Delete tail:

    previous.next = current.next
    tail = previous

Circular singly linked list gives `O(1)` append and prepend when a tail pointer is maintained, but deleting the tail by value is still `O(n)` because the previous node must be found.

---

# 30. Git

Suggested files:

`Notes/33-Circular-Linked-List.md`

`Practice/33-Circular-Linked-List.py`

Git commands:

    git add Notes/33-Circular-Linked-List.md Practice/33-Circular-Linked-List.py

    git commit -m "feat: add circular linked list"

    git push

Suggested commit message:

`feat: add circular linked list`
