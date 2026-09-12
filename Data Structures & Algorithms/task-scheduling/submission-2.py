class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import Counter, deque
        import heapq

        cnt = Counter(tasks)
        maxHeap = []

        for key, value in cnt.items():
            heapq.heappush(maxHeap, -value)
        
        que = deque()
        curr_time = 0

        while maxHeap or que:
            if not maxHeap:
                curr_time = que[0][1]
            else:
                count = heapq.heappop(maxHeap)
                if count != -1:
                    que.append([count + 1, curr_time + n + 1])
                curr_time += 1

            if que and que[0][1] <= curr_time:
                count, _ = que.popleft()
                heapq.heappush(maxHeap, count)
        return curr_time


            
