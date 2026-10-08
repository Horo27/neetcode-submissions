class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_ = sum(nums)
        return int(len(nums) * (len(nums) + 1) / 2 - sum_)