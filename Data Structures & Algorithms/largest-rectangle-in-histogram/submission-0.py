class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        small_left = [-1 for _ in range(n)]
        stack = []

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                small_left[i] = stack[-1]
            stack.append(i)
        
        heights.reverse()
        
        small_right = [n for _ in range(n)]
        stack = []

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                small_right[i] = n - 1 - stack[-1]
            stack.append(i)
        small_right.reverse()
        
        max_ = 0

        heights.reverse()

        for i in range(n):
            left = small_left[i]
            right = small_right[i]
            max_ = max(max_, (right - left - 1) * heights[i])
        return max_
        
        
            