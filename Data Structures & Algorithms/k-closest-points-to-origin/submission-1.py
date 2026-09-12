class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        import math

        maxHeap = []

        def distance(x, y):
            return math.sqrt(x**2 + y**2)
        
        for x, y in points:
            heapq.heappush(maxHeap, [-distance(x,y), [x, y]])
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        res = [pair for _, pair in maxHeap]
        return res