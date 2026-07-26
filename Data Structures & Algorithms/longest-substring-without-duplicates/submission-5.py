class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()

        if not s:
            return 0

        left, right = 0, 0
        substring.add(s[left])
        max_ = 1

        while right < len(s):
            if left == right:
                right += 1
            else:
                while s[right] in substring:
                    substring.remove(s[left])
                    left += 1
            
                substring.add(s[right])
                max_ = max(max_, (right - left + 1))
                right += 1
        
        return max_

