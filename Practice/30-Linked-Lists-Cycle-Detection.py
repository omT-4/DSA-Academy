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
            return new_node

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return new_node

    def display(self, limit=20):
        current = self.head
        count = 0

        while current is not None and count < limit:
            print(current.data, end=" -> ")
            current = current.next
            count += 1

        if current is not None:
            print("... (possible cycle)")
        else:
            print("None")

    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                return True

        return False


# Test 1: Linked list without a cycle
ll1 = LinkedList()

for value in [5, 10, 15, 20]:
    ll1.append(value)

print("List 1:")
ll1.display()
print("Has cycle:", ll1.has_cycle())


# Test 2: Linked list with a cycle
ll2 = LinkedList()

nodes = []
for value in [10, 20, 30, 40, 50]:
    nodes.append(ll2.append(value))

# Connect the last node back to node 20
nodes[-1].next = nodes[1]

print("\nList 2: Cyclic linked list")
print("Has cycle:", ll2.has_cycle())


# Test 3: Empty linked list
ll3 = LinkedList()

print("\nList 3: Empty linked list")
print("Has cycle:", ll3.has_cycle())


# Test 4: Single node pointing to itself
ll4 = LinkedList()
node = ll4.append(100)
node.next = node

print("\nList 4: Single-node cycle")
print("Has cycle:", ll4.has_cycle())

# List 1:
# 5 -> 10 -> 15 -> 20 -> None
# Has cycle: False

# List 2: Cyclic linked list
# Has cycle: True

# List 3: Empty linked list
# Has cycle: False

# List 4: Single-node cycle
# Has cycle: True

