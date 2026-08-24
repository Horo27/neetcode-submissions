class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []

        def backt(arr, k):
            nonlocal res
            res.append(arr[:])
            for i in range(k+1, len(nums)):
                arr.append(nums[i])
                backt(arr, i)
                arr.pop()
        backt([], -1)
        return res