class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracketMap = {")": "(", "}": "{", "]": "["}

        for ele in s:
            if ele in bracketMap:
                if stack and stack[-1] == bracketMap[ele]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ele)
        return True if not stack else False