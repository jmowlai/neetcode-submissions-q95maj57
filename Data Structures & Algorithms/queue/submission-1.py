class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.length = 0

    def isEmpty(self) -> bool:
        return self.length == 0 

    def append(self, value: int) -> None:
        new_node = Node(value)

        prev_node = self.tail.prev
        next_node = self.tail

        new_node.next = next_node
        new_node.prev = prev_node

        prev_node.next = new_node
        next_node.prev = new_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)

        prev_node = self.head
        next_node = self.head.next

        new_node.next = next_node
        new_node.prev = prev_node

        prev_node.next = new_node
        next_node.prev = new_node
        self.length += 1
        
    def pop(self) -> int:
        if self.length > 0:
            curr_node = self.tail.prev
            next_node = self.tail.prev.prev
            self.tail.prev = next_node
            next_node.next = self.tail
            self.length -= 1
            return curr_node.val
        else:
            return -1

    def popleft(self) -> int:
        if self.length > 0:
            curr_node = self.head.next
            next_node = self.head.next.next 
            self.head.next = next_node
            next_node.prev = self.head
            self.length -= 1
            return curr_node.val
        else:
            return -1