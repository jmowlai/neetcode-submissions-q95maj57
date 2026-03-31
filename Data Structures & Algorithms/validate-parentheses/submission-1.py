class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictMap = {')' : '(', ']' : '[', '}' : '{'}

        for c in s:
            if c in dictMap:
                if stack and stack[-1] == dictMap[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False