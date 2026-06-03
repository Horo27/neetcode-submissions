class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        dict_ = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }

        for c in s:
            if c in '([{':
                stack.append(c)
            else:
                if not stack or stack[-1] != dict_[c]:
                    return False
                stack.pop()

        if stack:
            return False
        return True