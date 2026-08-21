class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq

        window = [[-nums[i], i] for i in range(k)]

        heapq.heapify(window)

        l, r = 0, k - 1
        result = []

        while r < len(nums):
            while l > window[0][1]:
                heapq.heappop(window)
            
            result.append(-window[0][0])
            r += 1
            l += 1
            if r < len(nums):
                heapq.heappush(window, [-nums[r], r])
        return result
                