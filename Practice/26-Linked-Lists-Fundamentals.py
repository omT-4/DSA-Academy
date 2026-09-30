# ============================================================
# DSA - Lesson 26
# Linked Lists Fundamentals
# ============================================================


# ============================================================
# 1. NODE
# ============================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# ============================================================
# 2. LINKED LIST
# ============================================================

class LinkedList:
    def __init__(self):
        self.head = None

    # --------------------------------------------------------
    # APPEND
    # --------------------------------------------------------

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # --------------------------------------------------------
    # DISPLAY
    # --------------------------------------------------------

    def display(self):
        current = self.head

        while current is not None:
            print(current.data)
            current = current.next


# ============================================================
# 3. BASIC IMPLEMENTATION
# ============================================================

my_list = LinkedList()

my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print("Linked List:")
my_list.display()


# ============================================================
# 4. PRACTICE 1 — CREATE YOUR OWN LIST
# ============================================================

# Create another LinkedList.
#
# Append:
# 5
# 10
# 15
# 20
#
# Then display the list.


# ============================================================
# 5. PRACTICE 2 — MANUAL TRACING
# ============================================================

# Given:
#
# 10 → 20 → 30 → 40 → None
#
# Answer:
#
# 1. What does head point to?
#
# 2. What does head.next point to?
#
# 3. What does head.next.next point to?
#
# 4. What is head.next.next.data?
#
# 5. What is head.next.next.next.data?


# ============================================================
# 6. PRACTICE 3 — TRACE current
# ============================================================

# Given:
#
# 10 → 20 → 30 → None
#
# Start:
#
# current = head
#
# Trace current after each:
#
# current = current.next
#
# Write down:
#
# Step 1:
# Step 2:
# Step 3:
# Step 4:


# ============================================================
# 7. PRACTICE 4 — EMPTY LIST
# ============================================================

# Create an empty LinkedList.
#
# Call display().
#
# Observe what happens.


# ============================================================
# 8. PRACTICE 5 — COMPLEXITY
# ============================================================

# Explain in your own words:
#
# 1. Why is Linked List access O(n)?
#
# 2. Why is searching O(n)?
#
# 3. Why is traversal O(n)?
#
# 4. Why is our current append() O(n)?
# 
# 5. Why can insertion at the beginning be O(1)?


# ============================================================
# 9. CHALLENGE — WRITE FROM MEMORY
# ============================================================

# Without looking at the notes:
#
# Write the following from scratch:
#
# 1. Node class
# 2. LinkedList class
# 3. append()
# 4. display()
#
# Then create:
#
# 10 → 20 → 30 → 40 → None
#
# and display the values.