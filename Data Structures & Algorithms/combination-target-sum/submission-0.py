class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        
        def backt(arr, sum_, k):

            if sum_ == target:
                res.append(arr[:])
                return 

            for i in range(k, len(nums)):
                if sum_ + nums[i] <= target:
                    arr.append(nums[i])
                    backt(arr, sum_ + nums[i], i)
                    arr.pop()
        backt([], 0, 0)
        return res  