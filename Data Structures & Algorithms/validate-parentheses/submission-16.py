class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in {'{', '[', '('}:
                stack.append(i)
            else:
                if stack:
                    if i == '}':
                        if stack[-1] != '{':
                            return False
                        else:
                            stack.pop()
                    elif i == ']':
                        if stack[-1] != '[':
                            return False
                        else:
                            stack.pop()
                    elif i == ')':
                        if stack[-1] != '(':
                            return False
                        else:
                            stack.pop()
                else:
                    return False
        return True if not stack else False