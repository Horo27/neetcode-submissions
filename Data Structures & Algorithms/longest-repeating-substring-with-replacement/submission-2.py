class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def max_substring(c):
            left, right = 0, 0
            avail = k
            max_s = 0

            while right < len(s):          
                if s[right] != c:
                    if avail:
                        avail -=1
                        right +=1
                    else:
                        if s[left] != c:
                            avail += 1
                        left += 1
                else:
                    right += 1
                max_s = max(max_s, right - left)
            return max_s
        
        import string
        max_s = 0
        for letter in string.ascii_uppercase:
            max_s = max(max_s, max_substring(letter))
        return max_s