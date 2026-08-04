class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seq = {}
        seen = set()

        for num in nums:
            seen.add(num)
        
        max_ = 0

        for num in nums:
            if num - 1 not in seen:
                len_ = 0
                while num in seen:
                    len_ += 1
                    num +=1
                max_ = max(max_, len_)

        return max_