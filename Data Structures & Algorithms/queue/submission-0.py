class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.left = Node(-1)
        self.right = Node(-1)
        self.left.next = self.right
        self.right.prev = self.left
        self.length = 0

    def isEmpty(self) -> bool:
        if self.length == 0:
            return True
        else:
            return False
        

    def append(self, value: int) -> None:
        new_node = Node(value)
        prev_node = self.right.prev

        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = self.right
        self.right.prev = new_node
        self.length += 1

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        next_node = self.left.next

        next_node.prev = new_node
        new_node.next = next_node

        new_node.prev = self.left
        self.left.next = new_node
        self.length += 1

    def pop(self) -> int:
        if self.length <= 0:
            return -1
        else:
            last_node = self.right.prev
            value = last_node.value
            prev_node = last_node.prev
            prev_node.next = self.right
            self.right.prev = prev_node
            self.length -= 1
            return value

    def popleft(self) -> int:
        if self.length <= 0:
            return -1
        else:
            first_node = self.left.next
            value = first_node.value
            next_node = first_node.next
            next_node.prev = self.left
            self.left.next = next_node
            self.length -= 1
            return value
        
