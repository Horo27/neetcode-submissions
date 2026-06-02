class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}

        for i, num in enumerate(nums):
            if hmap.get(target - num, -1) != -1:
                return [hmap[target - num], i]
            hmap[num] = i

