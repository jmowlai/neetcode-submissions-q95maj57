class Solution:
    def isValid(self, s: str) -> bool:
        bracMap = {'}':'{', ']':'[', ')':'('}
        stack = []
        for i in s:
            if i not in bracMap:
                stack.append(i)
            elif stack:
                if stack[-1] != bracMap[i]:
                    return False
                else:
                    stack.pop()
            else:
                return False 
        return not stack




        