class Solution:
    def checkValidString(self, s: str) -> bool:
        hi, lo = 0, 0

        for c in s:
            if c == '(':
                hi += 1
                lo += 1
            elif c == ')':
                hi -= 1
                lo -= 1
            else:
                hi += 1
                lo -= 1
            # print(hi, lo)
            if hi < 0:
                return False
            lo = max(lo, 0)
        if hi == 0 or lo == 0:
            return True
        return False