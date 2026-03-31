class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res = 0
        stack = []
        for op in operations:
            if op == '+':
                tmp = stack[-1] + stack[-2]
                stack.append(tmp)
                res += tmp
            elif op == 'C':
                res -= stack.pop()
            elif op == 'D':
                tmp = stack[-1] * 2
                stack.append(tmp)
                res += tmp
            else:
                stack.append(int(op))
                res += int(op)
        
        return res
