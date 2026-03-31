class Solution:
    def isValid(self, s: str) -> bool:
        closedSet = {'}': '{', ']': '[', ')': '('}
        stack = []
        for i in s:
            if i in closedSet:
                if stack and stack[-1] == closedSet[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False