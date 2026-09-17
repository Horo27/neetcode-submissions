class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        words = set()
        k = 0

        for word in wordDict:
            k = max(k, len(word))
            words.add(word)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            if dp[i - 1]:
                for j in range(i , min(i + k, len(s) + 1)):
                    if s[i-1:j] in words:
                        dp[j] = True
        print(dp)
        return dp[-1]