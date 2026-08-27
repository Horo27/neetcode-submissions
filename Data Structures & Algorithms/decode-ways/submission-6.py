class Solution:
    def numDecodings(self, s: str) -> int:
        if not int(s[0]):
            return 0
        prev1 = 1
        prev2 = 1

        for i in range(1, len(s)):
            if not int(s[i]) and not (10 <= int(s[i-1] + s[i]) <= 26):
                return 0
            curr = 0
            if int(s[i]):
                curr += prev1
            if 10 <= int(s[i-1] + s[i]) <= 26:
                curr += prev2
            prev2 = prev1
            prev1 = curr
        return prev1