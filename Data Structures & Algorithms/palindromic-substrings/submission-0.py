class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[True] * len(s) for _ in range(len(s))]
        count = 0
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if j - i + 1 <= 3:
                    dp[i][j] = (s[i] == s[j])
                else:
                    dp[i][j] = dp[i+1][j-1] and s[i] == s[j]
                if dp[i][j]:
                    count += 1
        return count