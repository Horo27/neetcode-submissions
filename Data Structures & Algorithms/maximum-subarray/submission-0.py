class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ , curr = nums[0], nums[0]

        for i in range(1, len(nums)):
            curr = max(nums[i], curr + nums[i])
            max_ = max(max_, curr)
        return max_