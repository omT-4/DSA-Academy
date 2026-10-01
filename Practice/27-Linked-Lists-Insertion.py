# Lesson 27: Linked Lists — Insertion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end (without tail)
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert at a specific zero-based position
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

    # Display the linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Example usage
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(40)

print("Original list:")
ll.display()

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:")
ll.display()

ll.insert_at_position(30, 3)
print("After inserting 30 at position 3:")
ll.display()

ll.insert_at_position(50, 5)
print("After inserting 50 at the end:")
ll.display()

ll.insert_at_position(99, 10)  # Invalid position
ll.insert_at_position(99, -1)  # Invalid position


# Practice exercises:
# 1. Insert 15 at position 2 in 10 -> 20 -> 30.
# 2. Insert a node at position 0 in an empty list.
# 3. Insert a node at the end of a one-node list.
# 4. Try inserting at position n + 1 and observe the result.
# 5. Implement a separate LinkedList class with a tail pointer
#    and write an O(1) append method.
