class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backt(arr, k):
            res.append(arr[:])
            for i in range(k + 1, len(nums)):
                if i > 0 and nums[i] == nums[i - 1] and i != k + 1:
                    continue
                arr.append(nums[i])
                backt(arr, i)
                arr.pop()
        backt([], -1)
        return res
            