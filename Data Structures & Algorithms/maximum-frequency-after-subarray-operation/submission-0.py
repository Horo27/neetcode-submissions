class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        k_count = 0

        for num in nums:
            if num == k:
                k_count += 1
        max_ = k_count

        for i in range(1, 51):
            if i == k:
                continue
            curr = 0
            for num in nums:
                if num == k:
                    curr -= 1
                elif num == i:
                    curr += 1
                curr = max(curr, 0)
                max_ = max(max_, k_count + curr)
        return max_