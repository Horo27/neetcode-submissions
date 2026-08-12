class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[left] <= nums[right]: #not rotated
                return nums[left]

            if nums[mid] >= nums[left]:
                if nums[mid] > nums[mid + 1]:
                    return nums[mid + 1]
                left = mid + 1
            else:
                if nums[mid] < nums[mid - 1]:
                    return nums[mid]
                right = mid - 1
            
        