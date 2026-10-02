# Day 28: Linked Lists — Deletion

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
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

    # Delete at end
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

    # Delete at a zero-based position
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


# Testing
ll = LinkedList()

for value in [10, 20, 30, 40, 50]:
    ll.append(value)

print("Original list:")
ll.display()

print("Delete at beginning:")
ll.delete_at_beginning()
ll.display()

print("Delete at end:")
ll.delete_at_end()
ll.display()

print("Delete at position 1:")
ll.delete_at_position(1)
ll.display()

print("Delete at invalid position:")
ll.delete_at_position(10)
ll.display()
