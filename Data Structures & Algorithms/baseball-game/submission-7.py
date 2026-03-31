class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                val = stack[-1] + stack[-2]
                stack.append(val)
                res += val
            elif op == 'D':
                val = stack[-1] * 2
                stack.append(val)
                res += val
            elif op == 'C':
                res -= stack.pop()
            else:
                stack.append(int(op))
                res += int(op)
        return res 
            
                