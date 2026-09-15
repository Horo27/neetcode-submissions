class MedianFinder:

    def __init__(self):
        import heapq
        self.minHeap = []
        self.maxHeap = []

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -1 * num)
        if len(self.minHeap) - len(self.maxHeap) > 1:
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
        elif len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.minHeap[0] - self.maxHeap[0]) / 2
        if len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        return -self.maxHeap[0]
         


        