class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        # Sentinal Nodes for easier edge cases
        self.head = Node(-1)
        self.tail = Node(-1)
        # Setting up pointers for head/tail
        self.head.next = self.tail
        self.tail.prev = self.head
        # Creating length for O(1) checks
        self.length = 0

    def isEmpty(self) -> bool:
        # Queue is empty when self.length == 0
        return self.length == 0

    def append(self, value: int) -> None:
        # Create a new node
        new_node = Node(value)
        # Previous node is before the tail
        prev_node = self.tail.prev

        # Adding pointers for the new node inbetween sentinal and previous node
        new_node.next = self.tail
        new_node.prev = prev_node

        # Adding pointers for the existing nodes to the new node
        self.tail.prev = new_node
        prev_node.next = new_node
        # Add length +1
        self.length += 1
        
    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        next_node = self.head.next

        new_node.prev = self.head
        new_node.next = next_node

        self.head.next = new_node
        next_node.prev = new_node
        self.length += 1
        
    def pop(self) -> int:
        if self.isEmpty():
            return -1
        else:
            node = self.tail.prev
            prev_node = node.prev
            prev_node.next = self.tail
            self.tail.prev = prev_node
            self.length -= 1
            return node.val

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        else:
            node = self.head.next
            next_node = node.next
            next_node.prev = self.head
            self.head.next = next_node
            self.length -= 1
            return node.val
        
