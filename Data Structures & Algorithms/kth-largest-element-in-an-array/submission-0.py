class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq

        minHeap = []
        seen = {}

        for num in nums:
            seen[num] = seen.get(num, 0) + 1
            heapq.heappush(minHeap, [num, seen[num]])
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        return minHeap[0][0]