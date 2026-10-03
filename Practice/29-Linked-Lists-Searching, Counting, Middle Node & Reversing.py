# def search(self, target):
#     current = self.head
#     position = 0

#     while current is not None:
#         if current.data ==  target:
#             return position
#         current = current.next
#         position = position + 1

#     return - 1

# def count(self):
#     current = self.head
#     count = 0 
#     while current is not None:
#         count+=1
#         current = current.next
#     return count

# def find_middle(self):
#     fast = self.head
#     slow = self.head

#     while fast is not None and fast.next is not None:
#         fast = fast.next.next
#         slow = slow.next
#     return slow

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

    def search(self, target):
        current = self.head
        position = 0

        while current is not None:
            if current.data == target:
                return position

            current = current.next
            position += 1

        return -1

    def count_nodes(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.next

        return count

    def find_middle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse(self):
        prev = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev


# Testing
ll = LinkedList()

for value in [5, 10, 15, 20, 25]:
    ll.append(value)

print("Original list:")
ll.display()

print("Search for 15:", ll.search(15))
print("Search for 100:", ll.search(100))
print("Number of nodes:", ll.count_nodes())

middle = ll.find_middle()
if middle is not None:
    print("Middle node:", middle.data)
else:
    print("List is empty")

ll.reverse()
print("Reversed list:")
ll.display()

# Original list:
# 5 -> 10 -> 15 -> 20 -> 25 -> None
# Search for 15: 2
# Search for 100: -1
# Number of nodes: 5
# Middle node: 15
# Reversed list:
# 25 -> 20 -> 15 -> 10 -> 5 -> None

