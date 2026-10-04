
# Lesson 32: Doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.tail = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    # Insert at a specific index
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

    # Display from head to tail
    def display_forward(self):
        current = self.head

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.next

        print("None")

    # Display from tail to head
    def display_backward(self):
        current = self.tail

        while current is not None:
            print(current.data, end=" <-> ")
            current = current.prev

        print("None")

    # Search for a value
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return current
            current = current.next

        return None

    # Delete a node by value
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


# Testing the Doubly Linked List
dll = DoublyLinkedList()

dll.append(10)
dll.append(20)
dll.append(30)

print("Initial list:")
dll.display_forward()

dll.prepend(5)
print("After prepending 5:")
dll.display_forward()

dll.insert_at(2, 15)
print("After inserting 15 at index 2:")
dll.display_forward()

print("Backward traversal:")
dll.display_backward()

print("Search for 20:")
found = dll.search(20)
print(found.data if found else "Not found")

dll.delete(20)
print("After deleting 20:")
dll.display_forward()

dll.delete(5)
print("After deleting head:")
dll.display_forward()

dll.delete(30)
print("After deleting tail:")
dll.display_forward()

# Test deleting the final remaining nodes
dll.delete(10)
dll.delete(15)
print("After deleting all nodes:")
dll.display_forward()

print("Head:", dll.head)
print("Tail:", dll.tail)
