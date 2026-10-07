class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
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

        if self.head is self.tail:
            self.tail = None
            self.head = None
            return True

        if current is self.head:
            self.head = self.head.next
            self.tail.next = self.head
            self.head.prev = self.tail
            return True
        elif current is self.tail:
            self.tail = self.tail.prev
            self.tail.next = self.head 
            self.head.prev = self.tail
            return True
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
            count+=1
            if current is self.head:
                break
        return count

# Node
# CircularDoublyLinkedList
#     ├── append()
#     ├── prepend()
#     ├── display_forward()
#     ├── display_backward()
#     ├── search()
#     ├── count()
#     └── delete()

    def append(self, value):
        new_node = Node(value)

        # Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        # Non-empty list
        new_node.prev = self.tail
        new_node.next = self.head

        self.tail.next = new_node
        self.head.prev = new_node

        self.tail = new_node

    def prepend(self, value):
        new_node = Node(value)

        # Empty list
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            return

        # Non-empty list
        new_node.prev = self.tail
        new_node.next = self.head

        self.head.prev = new_node
        self.tail.next = new_node

        self.head = new_node

    def display_forward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        while True:
            print(current.data, end = "->")
            current = current.next
            if current is self.head:
                print("(back to head)")
                break

    def display_backward(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.tail
        while True:
            print(current.data, end= "->")
            current = current.prev
            if current is self.tail:
                print("(back to tail)")
                break

cdll = CircularDoublyLinkedList()

cdll.append(10)
cdll.append(20)
cdll.append(30)

cdll.display_forward()
print()

cdll.display_backward()
print()

print("Count:", cdll.count())
print("Search 20:", cdll.search(20))
print("Search 50:", cdll.search(50))

cdll.delete(20)

cdll.display_forward()
print()

cdll.display_backward()

# cdll = CircularDoublyLinkedList()

# cdll.append(10)
# cdll.append(20)
# cdll.append(30)

# cdll.delete(10)   # delete head

# cdll.display_forward()
# cdll.display_backward()

# cdll = CircularDoublyLinkedList()

# cdll.append(10)

# cdll.delete(10)

# print(cdll.head)
# print(cdll.tail)

