# Lesson 26 — Linked Lists Fundamentals

## 1. What is a Linked List?

A Linked List is a linear data structure made up of **nodes**.

Each node contains two things:

1. `data` → the value stored in the node
2. `next` → a reference to the next node

Example:

```text
10 → 20 → 30 → 40 → None
```

`None` means there is no next node.

Unlike an array, a Linked List does not use indexes to directly access elements.

---

# 2. What is a Node?

A Node is one individual element of a Linked List.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

A Node looks conceptually like:

```text
┌───────────────┐
│ data │ next   │
└───────────────┘
```

For:

```python
node = Node(10)
```

we initially have:

```text
┌───────────────┐
│ data = 10     │
│ next = None   │
└───────────────┘
```

---

# 3. Understanding `__init__`

`__init__` automatically runs when an object is created.

Example:

```python
node1 = Node(10)
```

Python automatically calls the `__init__` method.

```python
def __init__(self, data):
    self.data = data
    self.next = None
```

Its job is to initialize the newly created object.

### Simple meaning

```text
__init__
→ Set the object up when it is created.
```

---

# 4. Understanding `self`

`self` refers to the **particular object** currently being created or used.

Example:

```python
node1 = Node(10)
node2 = Node(20)
```

Conceptually:

```text
node1
 ↓
data = 10
next = None


node2
 ↓
data = 20
next = None
```

When we write:

```python
self.data = data
```

it means:

> Put the given data into this particular object.

When we write:

```python
self.next = None
```

it means:

> This particular node currently has no next node.

---

# 5. Connecting Nodes

Nodes are connected using `.next`.

Example:

```python
node1.next = node2
node2.next = node3
```

Suppose:

```python
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
```

After connecting:

```text
10 → 20 → 30 → None
```

The connections are:

```text
node1.next → node2
node2.next → node3
node3.next → None
```

---

# 6. The `head`

`head` points to the **first node** of the Linked List.

Example:

```python
head = node1
```

Structure:

```text
head
 ↓
10 → 20 → 30 → None
```

The `head` does not contain the entire list.

It points to the first node, and from that node we can follow `.next` to reach the remaining nodes.

---

# 7. Why is `head` important?

A Linked List can be accessed by starting from its first node.

```text
head
 ↓
10 → 20 → 30 → 40 → None
```

If we lose `head`, we no longer have a direct starting point from which to traverse the list.

Therefore:

```text
head → first node
```

---

# 8. Traversal

Traversal means **visiting the nodes one by one**.

Basic traversal:

```python
current = head

while current is not None:
    print(current.data)
    current = current.next
```

Suppose:

```text
10 → 20 → 30 → None
```

Initially:

```text
10 → 20 → 30 → None
↑
current
```

After:

```python
current = current.next
```

we move to:

```text
10 → 20 → 30 → None
     ↑
   current
```

Then:

```text
10 → 20 → 30 → None
          ↑
        current
```

Then:

```text
current → None
```

The loop stops.

---

# 9. Understanding `current`

`current` is a variable that points to the node we are **currently visiting**.

Think of `current` as your finger pointing at a node.

```text
10 → 20 → 30 → 40 → None
↑
current
```

After:

```python
current = current.next
```

the finger moves forward:

```text
10 → 20 → 30 → 40 → None
     ↑
   current
```

Then:

```text
10 → 20 → 30 → 40 → None
          ↑
        current
```

---

# 10. `current`, `current.data`, and `current.next`

These are different things.

```text
10 → 20 → 30 → None
↑
current
```

### `current`

Points to the Node containing `10`.

### `current.data`

Gets the value stored inside the current Node.

```python
current.data
```

Result:

```text
10
```

### `current.next`

Gets the next Node.

```python
current.next
```

Result:

```text
Node containing 20
```

---

# 11. `current.next is None` vs `current is None`

This distinction is very important.

## `current.next is None`

Means:

> `current` is the **last node**.

Example:

```text
10 → 20 → 30 → None
          ↑
        current
```

Here:

```python
current.next is None
```

is `True`.

---

## `current is None`

Means:

> We have gone **past the last node**.

```text
10 → 20 → 30 → None
                 ↑
              current
```

Here:

```python
current is None
```

is `True`.

### Remember:

```text
current.next is None
→ current is the last node

current is None
→ current is past the last node
```

---

# 12. Creating a LinkedList Class

Instead of managing `head` separately, we can create a class representing the entire Linked List.

```python
class LinkedList:
    def __init__(self):
        self.head = None
```

When we create:

```python
my_list = LinkedList()
```

the list is empty:

```text
head → None
```

---

# 13. Why is `self.head = None`?

A newly created Linked List has no nodes.

Therefore:

```python
self.head = None
```

means:

> This Linked List currently has no first node.

Later, after adding a node:

```text
head
 ↓
10 → None
```

---

# 14. Append

`append()` means adding a new node at the **end** of the Linked List.

Implementation:

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

---

# 15. Understanding `append()` for the First Node

Suppose:

```python
my_list = LinkedList()
```

Initially:

```text
head → None
```

Now:

```python
my_list.append(10)
```

First:

```python
new_node = Node(10)
```

creates:

```text
10 → None
```

The list is empty:

```python
self.head is None
```

Therefore:

```python
self.head = new_node
```

Result:

```text
head
 ↓
10 → None
```

Then:

```python
return
```

stops the function.

---

# 16. Why is `return` Necessary?

For the first node, the list is empty.

There is no existing node to traverse.

Therefore, after:

```python
self.head = new_node
```

we stop the function.

Without the `return`, the code would continue into the traversal section unnecessarily.

---

# 17. Appending a Second Node

Suppose we already have:

```text
head
 ↓
10 → None
```

Now:

```python
my_list.append(20)
```

creates:

```text
20 → None
```

The list is not empty, so:

```python
if self.head is None:
```

is `False`.

We then execute:

```python
current = self.head
```

Therefore:

```text
head
 ↓
10 → None
↑
current
```

Now:

```python
while current.next is not None:
```

For node `10`:

```text
10.next → None
```

Therefore the condition is `False`.

The loop doesn't run.

Then:

```python
current.next = new_node
```

connects:

```text
10 → 20 → None
```

---

# 18. Appending a Third Node

Suppose:

```text
head
 ↓
10 → 20 → None
```

Now:

```python
my_list.append(30)
```

creates:

```text
30 → None
```

Then:

```python
current = self.head
```

so:

```text
10 → 20 → None
↑
current
```

Check:

```python
current.next is not None
```

10's next is 20, so the condition is `True`.

Move:

```python
current = current.next
```

Now:

```text
10 → 20 → None
     ↑
   current
```

20's next is `None`, so the loop stops.

Then:

```python
current.next = new_node
```

Result:

```text
10 → 20 → 30 → None
```

---

# 19. Important `append()` Mental Model

Every time we call:

```python
my_list.append(value)
```

we:

1. Create a new Node.
2. If the list is empty → make it the `head`.
3. Otherwise → start at `head`.
4. Move to the last existing node.
5. Connect the last node to the new Node.

Example:

```python
my_list.append(10)
my_list.append(20)
my_list.append(30)
```

Result:

```text
head
 ↓
10 → 20 → 30 → None
```

---

# 20. `current` Does Not Automatically Move

Suppose:

```text
10 → 20 → 30 → 40 → None
          ↑
        current
```

If we execute:

```python
current.next = new_node
```

we change the connection after `current`.

We do **not** move `current`.

For example:

```text
current
   ↓
30 → 40
```

After connecting a new node:

```text
current
   ↓
30 → 40 → 50
```

`current` is still pointing to `30`.

---

# 21. Display

We can create a method to display all nodes:

```python
def display(self):
    current = self.head

    while current is not None:
        print(current.data)
        current = current.next
```

Example:

```python
my_list.display()
```

Output:

```text
10
20
30
40
```

---

# 22. Why Does Display Use `current is not None`?

For display, we want to process **every node**, including the last node.

Example:

```text
10 → 20 → 30 → None
```

We visit:

```text
10
20
30
```

Then `current` becomes `None`.

The loop stops.

Therefore:

```python
while current is not None:
```

is used.

---

# 23. Append Loop vs Display Loop

### Append

```python
while current.next is not None:
    current = current.next
```

Purpose:

> Find the last node.

Therefore, it stops **at the last node**.

```text
10 → 20 → 30 → None
          ↑
       current
```

---

### Display

```python
while current is not None:
    print(current.data)
    current = current.next
```

Purpose:

> Visit every node.

Therefore, it processes the last node and then moves to `None`.

---

# 24. Empty Linked List

Suppose:

```python
my_list = LinkedList()
```

We have:

```text
head → None
```

If we call:

```python
my_list.display()
```

then:

```python
current = self.head
```

gives:

```text
current → None
```

Therefore:

```python
while current is not None:
```

is immediately `False`.

Nothing is printed.

This is correct because the list contains no nodes.

---

# 25. One-Node Linked List

Example:

```text
head
 ↓
10 → None
```

During display:

```text
current → 10
```

Print:

```text
10
```

Then:

```python
current = current.next
```

Since:

```text
10.next → None
```

we get:

```text
current → None
```

The loop stops.

---

# 26. Following `.next`

Suppose:

```text
head
 ↓
10 → 20 → 30 → 40 → None
```

Then:

```python
head
```

→ Node containing `10`

```python
head.next
```

→ Node containing `20`

```python
head.next.next
```

→ Node containing `30`

```python
head.next.next.next
```

→ Node containing `40`

To get the value:

```python
head.next.next.data
```

→ `30`

And:

```python
head.next.next.next.data
```

→ `40`

### Mental model

```text
head
 ↓
next
 ↓
next
 ↓
data
```

Each `.next` follows one connection.

---

# 27. Linked List vs Array

## Array

An array provides direct access using indexes.

```text
Index:  0    1    2    3
       ┌────┬────┬────┬────┐
       │ 10 │ 20 │ 30 │ 40 │
       └────┴────┴────┴────┘
```

For example:

```python
arr[2]
```

directly accesses:

```text
30
```

Therefore:

```text
Array access → O(1)
```

---

## Linked List

A Linked List doesn't provide direct index-based access.

```text
10 → 20 → 30 → 40 → None
```

To reach `30`, we must start from `head`:

```text
10 → 20 → 30
```

We follow:

```text
head
 ↓
next
 ↓
next
```

Therefore:

```text
Linked List access → O(n)
```

---

# 28. Why is Linked List Access O(n)?

Suppose:

```text
10 → 20 → 30 → 40 → 50
```

To reach `50`, starting from `head`, we must follow the chain:

```text
10 → 20 → 30 → 40 → 50
```

If there are `n` nodes, reaching the target may require up to `n` steps.

For example:

```text
5 nodes → up to 5 steps
1,000 nodes → up to 1,000 steps
1,000,000 nodes → up to 1,000,000 steps
```

The number of operations grows with the number of elements.

Therefore:

```text
Access → O(n)
```

---

# 29. Search

Searching means checking whether a particular value exists.

Example:

```text
10 → 20 → 30 → 40 → None
```

To search for `40`:

```text
10 ❌
20 ❌
30 ❌
40 ✅
```

In the worst case, we may have to check every node.

Therefore:

```text
Search → O(n)
```

---

# 30. Traversal Complexity

Traversal visits every node:

```python
current = self.head

while current is not None:
    print(current.data)
    current = current.next
```

If there are `n` nodes, we visit `n` nodes.

Therefore:

```text
Traversal → O(n)
```

---

# 31. Append Complexity

Our current `append()` implementation starts at `head` and walks to the last node.

```python
current = self.head

while current.next is not None:
    current = current.next
```

For a list with `n` nodes, we may need to traverse the entire list.

Therefore:

```text
Append → O(n)
```

### Important

This is the complexity of **our current implementation**.

Later, we can maintain a `tail` pointer and make appending O(1).

---

# 32. Insert at Beginning

Suppose:

```text
head
 ↓
20 → 30 → 40 → None
```

We want to insert `10`.

Create:

```text
10 → None
```

Then:

```python
new_node.next = head
head = new_node
```

Result:

```text
head
 ↓
10 → 20 → 30 → 40 → None
```

We don't need to traverse the existing nodes.

Therefore:

```text
Insert at beginning → O(1)
```

Insertion will be covered in detail in a future Linked List lesson.

---

# 33. Complexity Summary

| Operation | Complexity | Why? |
|---|---:|---|
| Access | O(n) | Must follow nodes from head |
| Search | O(n) | May check every node |
| Traversal | O(n) | Visits every node |
| Append | O(n) | Our implementation traverses to the end |
| Insert at beginning | O(1) | Only references need to change |

### Important

Do not memorize:

```text
Linked List = O(n)
```

Complexity depends on the **operation** being performed.

---

# 34. Complete Code

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

my_list.display()
```

Output:

```text
10
20
30
40
```

---

# 35. Key Takeaways

```text
Node
→ data + next

head
→ points to the first node

current
→ points to the node currently being visited

current.data
→ value inside current node

current.next
→ next node

None
→ no next node
```

Linked List:

```text
head
 ↓
10 → 20 → 30 → 40 → None
```

Complexities:

```text
Access              → O(n)
Search              → O(n)
Traversal           → O(n)
Append (our version)→ O(n)
Insert at beginning → O(1)
```

### Core Mental Model

A Linked List is a chain of nodes.

Each node knows:

> "Here is my data, and here is where the next node is."

To move through the list:

```python
current = current.next
```

That single line moves us one node forward.