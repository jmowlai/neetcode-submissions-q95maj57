class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.index = 0    

    def push(self, val: int) -> None:
        self.stack.append(val)
        tmp = min(self.minStack[-1], val) if self.minStack else val 
        self.minStack.append(tmp)
        self.index += 1
        
    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minStack.pop()
            self.index -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]