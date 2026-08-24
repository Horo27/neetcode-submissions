class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backt(arr, seen):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            
            for num in nums:
                if num not in arr:
                    arr.append(num)
                    seen.add(num)
                    backt(arr, seen)
                    seen.remove(num)
                    arr.pop()

        backt([], set())
        return res