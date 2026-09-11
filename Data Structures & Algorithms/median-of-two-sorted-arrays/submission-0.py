class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        left, right = 0, len(nums1)

        while left <= right:
            mid1 = (left + right) // 2
            mid2 = (len(nums1) + len(nums2) + 1) // 2 - mid1

            left1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            right1 = nums1[mid1] if mid1 < len(nums1) else float('inf')
            left2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            right2 = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if left1 <= right2 and right1 >= left2:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return max(left1, left2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2
            if left1 > right2:
                right = mid1 - 1
            else:
                left = mid1 + 1