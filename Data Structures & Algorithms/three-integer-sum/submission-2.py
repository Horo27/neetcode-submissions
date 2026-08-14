class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)):
            if i and nums[i] == nums[i - 1]:
                continue
            
            left, right = i+1, len(nums) - 1

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    # if nums[i] != nums[left] != nums[right]:
                    sol.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right and nums[right] == nums[right + 1]:
                        right -= 1
                    
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1
        return sol

