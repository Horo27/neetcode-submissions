class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 1, 1
        res = nums[0]

        for num in nums:
            tmp = maxProd * num
            maxProd = max(num, tmp, minProd * num)
            minProd = min(num, minProd * num, tmp)
            res = max(res, maxProd)
            

        return res


