class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_ = 0

        for i in range(len(nums)):
            if i <= max_:
                max_ = max(max_, i + nums[i])
            else:
                break
    
        return True if max_ >= len(nums) - 1 else False