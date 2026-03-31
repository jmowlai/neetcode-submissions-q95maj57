class MinStack:

    def __init__(self):
        self.stack = []
        self.min = float('-inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(val, self.min)     

    def pop(self) -> None:
        tmp = self.stack.pop()
        if tmp < 0:
            self.min = self.min - tmp

    def top(self) -> int:
        if self.stack[-1] > 0:
            return self.stack[-1] + self.min
        else:
            return self.min
        
    def getMin(self) -> int:
        return self.min
        
