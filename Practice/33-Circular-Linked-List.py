# Lesson 33 - Circular Linked List
# Practice File

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1)
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

    # O(1)
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

    # O(n)
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

    # O(n)
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

    # O(n)
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

    # O(n)
    def delete(self, value):
        if self.head is None:
            return False

        current = self.head
        previous = self.tail

        # Find the node
        while True:
            if current.data == value:
                break

            previous = current
            current = current.next

            # Value not found
            if current is self.head:
                return False

        # Case 1: Only node
        if current is self.head and current is self.tail:
            self.head = None
            self.tail = None
            return True

        # Case 2: Delete head
        if current is self.head:
            self.head = current.next
            self.tail.next = self.head
            return True

        # Case 3: Delete middle or tail
        previous.next = current.next

        # If deleting tail
        if current is self.tail:
            self.tail = previous

        return True


# -----------------------------
# Testing
# -----------------------------

cll = CircularLinkedList()

print("Initial list:")
cll.display()

print("\nAppending 10, 20, 30:")
cll.append(10)
cll.append(20)
cll.append(30)
cll.display()

print("\nPrepending 5:")
cll.prepend(5)
cll.display()

print("\nSearch:")
print("20 exists:", cll.search(20))
print("50 exists:", cll.search(50))

print("\nCount:")
print("Number of nodes:", cll.count())

print("\nDelete head (5):")
cll.delete(5)
cll.display()

print("\nDelete middle (20):")
cll.delete(20)
cll.display()

print("\nDelete tail (30):")
cll.delete(30)
cll.display()

print("\nDelete remaining node (10):")
cll.delete(10)
cll.display()

print("\nFinal count:")
print(cll.count())