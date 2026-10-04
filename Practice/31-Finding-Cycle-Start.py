# Lesson 31: Finding the Starting Node of a Cycle
# Floyd's Tortoise and Hare Algorithm


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

    def detect_cycle_start(self):
        slow = self.head
        fast = self.head

        # Phase 1: Detect the cycle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow is fast:
                break
        else:
            return None

        # Phase 2: Find the cycle's starting node
        slow = self.head

        while slow is not fast:
            slow = slow.next
            fast = fast.next

        return slow


# Example 1: Linked list with a cycle
ll = LinkedList()

for value in [10, 20, 30, 40, 50, 60]:
    ll.append(value)

# Connect node 60 back to node 30
node_30 = ll.head.next.next
node_60 = ll.head

while node_60.next is not None:
    node_60 = node_60.next

node_60.next = node_30

cycle_start = ll.detect_cycle_start()

if cycle_start:
    print("Cycle starts at:", cycle_start.data)
else:
    print("No cycle detected")


# Example 2: Linked list without a cycle
ll2 = LinkedList()

for value in [5, 10, 15, 20]:
    ll2.append(value)

cycle_start = ll2.detect_cycle_start()

if cycle_start:
    print("Cycle starts at:", cycle_start.data)
else:
    print("No cycle detected")

# Cycle starts at: 30
# No cycle detected