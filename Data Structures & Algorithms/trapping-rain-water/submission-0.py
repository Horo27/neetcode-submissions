class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        maxleft, maxright = 0, 0
        total = 0

        while left <= right:
            maxleft = max(maxleft, height[left])
            maxright = max(maxright, height[right])
            if maxleft < maxright:
                total += maxleft - height[left]
                left += 1
            else:
                total += maxright - height[right]
                right -= 1
        return total
                